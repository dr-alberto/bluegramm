import requests

class API():        
    def info(token, url):
        headers = {'Authorization': f'Token {token}'}
        response = requests.post(url, headers=headers)
        return response
        
    def prediction(token, url, data):
        headers = {'Authorization': f'Token {token}'}
        data = {'content':data}
        response = requests.post(url, data=data, headers=headers)
        return response