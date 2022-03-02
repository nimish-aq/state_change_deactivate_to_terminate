"""
Created on 28-Feb-2022
@author: nimish.jain@airlinq.com

Script to generate auth token and call APIs for sim state change
"""
import requests
from config import auth_api_config, action_api_config
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class api_call:
    def __init__(self):
        self.token = self.auth()
    def auth(self):
        """
        Method to generate auth token
        :return: Auth token
        """
        token = ''
        data={
                "username": auth_api_config["username"],
                "password": auth_api_config["password"]
               }
        header ={'Content-Type': 'application/json'}
        #print(auth_api_config['authentication_api_url'])

        response = requests.post(auth_api_config['authentication_api_url'],
                                 headers=header,
                                 data = json.dumps(data),
                                 verify=False)

        if response.status_code == 200:
            auth_resp = json.loads(response.content)
            token = auth_resp["token"]
        return token

    def sim_state_change(self,data,token):
        """
        Method to call sim state change API
        :param data: API payload data
        :return: API Response code and payload
        """

        url = action_api_config["sim_state_change_url"]
        header = {'Content-Type': 'application/json',
                  'Authorization': token}
        status_code = 401
        retry = 2
        while status_code == 401 and retry:
            print(retry, url, header,data)
            response = requests.put(url,
                                 headers=header,
                                 data=json.dumps(data),
                                 verify=False)
            status_code = response.status_code
            content = json.loads(response.content)
            retry = retry - 1
            if status_code == 401 and retry:
                header["Authorization"] = self.token = self.auth()
        return status_code, content

    

