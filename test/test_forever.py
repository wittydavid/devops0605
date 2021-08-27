from time import sleep
import requests

while True:
    print("Hello")
    sleep(1)
    my_file = open("url.txt", "r")
    url_line = my_file.read()
    my_file.close()
    print(url_line)
    response = requests.get(str(url_line))
    if response.status_code != 200:
        print("somethings wrong")
