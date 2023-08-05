# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 20:07:52 2021

@author: Eli Shamis
"""


import requests
import json
from neurospeed.utils.api_config_service import ApiConfig

class HttpService:    
    
    def __init__(self):
        api_config = ApiConfig()

        self._api_url =  api_config.get_http_url()
        self._api_url = self._api_url + '/api'
    
    
    
    def GET_request(self, endpoint, params, headers = {}):
        api_url = self._api_url + endpoint
        print('doing HTTP GET to url:', api_url, 'with params:', params)
        
        response = None
        try:
            response = requests.get(api_url, headers=headers, params = params)
            response.raise_for_status()
      
            if (response.ok):
                response_parsed = json.loads(response.content)
                print('GET response from {} '.format(endpoint ))
                return response_parsed
    
            else:
                raise requests.exceptions.HTTPError
        
        except requests.exceptions.HTTPError as e:
            print('Failed to HTTP GET to url:', api_url)
            print (e.response.text)
            
            
    def POST_request(self, endpoint, payload, headers = {}):
        api_url = self._api_url + endpoint
        print('doing HTTP POST to url: {} payload {}'.format( api_url, payload ))

        response = None
        try:
            response = requests.post(api_url, data=payload, headers =headers)
            response.raise_for_status()
    
     
            if (response.ok):
                response_parsed = json.loads(response.content)
                print('POST response from {}  '.format(endpoint ))
                return response_parsed
    
            else:
                raise requests.exceptions.HTTPError
        
        except requests.exceptions.HTTPError as e:
            print('Failed to HTTP POST to url:', api_url)
            print (e.response.text)      
            
            
    def PUT_request(self, endpoint, payload, params, headers = {}):
        api_url = self._api_url + endpoint
        print('doing HTTP PUT to url:', api_url, 'with params:', params, 'and payload:', payload, '')
        
        response = None
        try:
            response = requests.put(api_url, data=payload, headers =headers, params=params)
            response.raise_for_status()
            if (response.ok):
                response_parsed = json.loads(response.content)
                print('PUT response from {} '.format(endpoint ))
                return response_parsed
    
            else:
                raise requests.exceptions.HTTPError
        
        except requests.exceptions.HTTPError as e:
            print('Failed to HTTP PUT to url:', api_url)
            print (e.response.text)      
            

    def DELETE_request(self, endpoint, params, headers = {}):
        api_url = self._api_url + endpoint
        print('doing HTTP DELETE to url:', api_url, 'with params:', params)
        
        response = None
        try:
            response = requests.delete(api_url, headers =headers, params=params)
            response.raise_for_status()

            if (response.ok):
                response_parsed = json.loads(response.content)
                print('DELETE response from {} '.format(endpoint ))
                return response_parsed
    
            else:
                raise requests.exceptions.HTTPError
        
        except requests.exceptions.HTTPError as e:
            print('Failed to HTTP DELETE to url:', api_url)
            print (e.response.text)       
  
   