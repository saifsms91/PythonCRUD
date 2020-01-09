import requests
url = 'https://jsonplaceholder.typicode.com/photos'

response = requests.get(url)
print(response.json())

#response = requests.request("GET", url)
#print(response)

