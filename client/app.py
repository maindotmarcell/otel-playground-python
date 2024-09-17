import time
import requests

def ping_server():
    while True:
        try:
            response = requests.get('http://server:34289/ping')
            print(f"Received response: {response.json()}")
        except requests.RequestException as e:
            print(f"Error: {e}")
        time.sleep(5)

if __name__ == '__main__':
    ping_server()