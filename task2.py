import  requests

base_url = 'https://httpbin.org/stream/1';

def get_delay():
    resp = requests.get(base_url)
    data = resp.json()
    print(data)


for _ in range(5)
get_delay()

print('Okay all finished getting...')