
import requests
url = 'https://jsonplaceholder.typicode.com/photos'
jsonPayLoad = {'albumId':1,'title':'testabc', 'url': 'abc.com','thumbnailUrl':'nothing.com'}
response = requests.post(url,json=jsonPayLoad)
print(response.json())
