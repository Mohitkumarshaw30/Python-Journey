# Install and import the requests module (if available) and use it to fetch data
# from "https://api.github.com" .

import requests

data = requests.get("https://api.github.com")
print(data.text)
