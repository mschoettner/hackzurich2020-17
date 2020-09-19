import requests
user = 'Bearer'
token = '8c35a7f0a5cf41a8d7e4c924e60dc7a04f08d006'
response = requests.get('https://api-beta.bite.ai/meals/',
                        headers = {'Authorization': 'Bearer 8c35a7f0a5cf41a8d7e4c924e60dc7a04f08d006'})
print(response)
