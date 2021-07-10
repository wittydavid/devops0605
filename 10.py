#    file name       class
from datetime import datetime
#      package name
import requests

print(datetime.now())
response = requests.get("https://github.com")
if response.status_code == 200:
    print("github is up and running")
