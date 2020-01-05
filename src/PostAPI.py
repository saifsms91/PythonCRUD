import requests
import json

url = "https://jsonplaceholder.typicode.com/photos?albumId=8"
headers = {
    "Content-type": "application/json; charset=UTF-8"
};
body = json.dumps({
    "title": "Wiki",
    "url": "https://tinyurl.com/vyu7woh",
    "albumId": "8"
});
response = requests.post(url, data=body, json=body)
print(response)
urlGet = "https://jsonplaceholder.typicode.com/photos"
responseGet = requests.request("GET", urlGet)
print(responseGet)
