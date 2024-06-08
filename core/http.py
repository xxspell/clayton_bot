import requests
class HttpClient:
    def __init__(self, user_agent=None, common_headers=None):
        self.headers = {}
        if user_agent:
            self.headers['User-Agent'] = user_agent
        if common_headers:
            self.headers.update(common_headers)

    def add_header(self, key, value):
        self.headers[key] = value

    def get(self, url, params=None):
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
        except requests.exceptions.RequestException as e:
            print(f"GET request to {url} failed: {e}")
            return None

    def post(self, url, data=None, json=None):
        try:
            response = requests.post(url, headers=self.headers, data=data, json=json)
            response.raise_for_status()
            return response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
        except requests.exceptions.RequestException as e:
            print(f"POST request to {url} failed: {e}")
            return None