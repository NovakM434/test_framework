import requests

class Api:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        return self.session.get(endpoint)

    def post(self, endpoint, data):
        return self.session.post(endpoint, data)

    def put(self, endpoint, data):
        return self.session.put(endpoint, data)

    def patch(self, endpoint, data):
        return self.session.patch(endpoint, data)

    def delete(self, endpoint):
        return self.session.delete(endpoint)

    def get_payload(self, response):
        return response.json()
