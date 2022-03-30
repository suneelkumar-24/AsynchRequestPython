import requests

# from timer import timer

url = 'https://httpbin.org/uuid'
stream_url = 'https://httpbin.org/stream/1'


def fetch(session, url):
    with session.get(url) as response:
        print(session ,' ', response.json()['uuid'])


def get_stream(session):
    with session.get(stream_url) as response:
        print(session ,' ', response.json())


# @timer(1,1)
def main():
    with requests.Session() as session:
        # print(session)
        for _ in range(10):
            fetch(session, url)
    
        for _ in range(10):
            get_stream(session)