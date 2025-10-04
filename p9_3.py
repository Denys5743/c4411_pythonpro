import urllib.request

import requests

response = requests.post ("https://httpbin.org/get")
            data="Test data"
            headers ={"h1": "Test title"})

print(response.text)


