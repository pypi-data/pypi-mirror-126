# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:42:25 2021

@author: Eli Shamis
"""

import socketio 
from neurospeed.utils.api_config_service import ApiConfig

class DownlinkRoom_AS_User_Handler:
    
    def __init__(self, user_auth_handler):
        self._contex = "DownlinkRoom_AS_User_Handler - "
        
        self._auth_handler = user_auth_handler
        self._username = self._auth_handler.get_username()
        self._connection_status = False
        self._downlink_router_external_handler = None
        
        # Create User_Downlink_Api and pass user configuration
        self._downlink_api = self.DownlinkRoom_Api(self._auth_handler)
        
    def downlinkRoom_connection_handler(self):
        print("{} User connected to user's {} DownlinkRoom".format(self._contex, self._username ))
        self._connection_status = True
    
    
    def downlinkRoom_disconnect_handler(self):
        print("{} User disconnected from user's {} DownlinkRoom".format(self._contex,self._username ))
        self._connection_status = False
    
    
    def downlinkRoom_router_handler(self, payload):
        print("{} message {} routed from customer to user: {}".format(self._contex, payload, self._username ))

        # propogate routed message to main program
        if (self._downlink_router_external_handler != None):
            self._downlink_router_external_handler(self, payload) # send current contex along with payload (current DownlinkRoom_AS_User_Handler instance) 


    def set_downlink_router_external_handler(self, handler):
        self._downlink_router_external_handler = handler
        
    def get_username(self):
        return self._username
    
    def connect(self):
        # attach relevant handlers for socket.io events
        self._downlink_api.set_connection_handler(self.downlinkRoom_connection_handler)
        self._downlink_api.set_disconnect_handler(self.downlinkRoom_disconnect_handler)
        self._downlink_api.set_downlink_handler(self.downlinkRoom_router_handler)

        # connect 
        self._downlink_api.connect()
        
    def disconnect(self):
        self._downlink_api.disconnect()
        
    def is_connected(self):
        return self._connection_status
    
    
    class DownlinkRoom_Api:
    
        def __init__(self, auth_handler):
            api_config = ApiConfig()
            
        
            self._access_token = auth_handler.get_access_token()
            self._username = auth_handler.get_username()
            self._socket_url = api_config.get_socket_url()
            
            logger_on = True
            if auth_handler.is_verbose_log() == False:
              logger_on = False
            self._sio = socketio.Client(logger=logger_on, engineio_logger=False, reconnection_delay  = 5, reconnection = True) 


            
        def set_connection_handler(self, handler):
            self._sio.on('connect',handler = handler)
            
        def set_disconnect_handler(self, handler):
            self._sio.on('disconnect', handler = handler)
            
        def set_downlink_handler(self, handler):
            self._sio.on('downlink', handler = handler)
         
            
        def connect(self):
           headers = {
               "jwt_token": self._access_token,  # required
           }
        
           print("Downlink_Api - Connecting to user's {} Downlink room as user ".format(self._username))
           self._sio.connect(url = self._socket_url, transports ='websocket', headers=headers, socketio_path= '/target_is_downlink_room_as_user' ) 
    
        def disconnect(self):
           self._sio.disconnect()
            