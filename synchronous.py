from urllib import request
import requests

from timer import timer

url = 'https://httpbin.org/uuid'

def fetch(session, url):
    with session.get(url) as response:
        print(response.json())

@timer(1,1)
def main():
    with requests.Session() as session:
        # print(session)
        for _ in range(10):
            fetch(session, url)



