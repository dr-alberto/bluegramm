import requests

class API():        
    def __init__(self, token, url):
        self.token = token
        self.url = url

    def info(self):
        headers = {'Authorization': f'Token {self.token}'}
        response = requests.post(self.url, headers=headers)
        return response
        
    def prediction(self, data):
        headers = {'Authorization': f'Token {self.token}'}
        data = {'content':data}
        response = requests.post(self.url, data=data, headers=headers)
        return response