import requests

url = "https://jsonplaceholder.typicode.com/photos/33"
response = requests.delete(url)
print(response.json())


