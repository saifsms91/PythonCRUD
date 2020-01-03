import requests

url = "https://jsonplaceholder.typicode.com/photos/351"

response = requests.delete(url)
print(response)
