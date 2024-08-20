import requests

base = "http://127.0.0.1:5000/"

response = requests.get(base + "helloworld/tim/ok")
print(response.json())

