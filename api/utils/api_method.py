from utils.api_base import Api


class ReqresApi(Api):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    def get_list_user(self, page_id):
        return self.get(f"{self.url}/api/users?page={page_id}")

    def get_single_user(self, user_id):
        return self.get(f"{self.url}/api/users/{user_id}")

    def get_resource_list(self):
        return self.get(f"{self.url}/api/unknown")

    def get_resource_single(self, resource_id):
        return self.get(f"{self.url}/api/unknown/{resource_id}")

    def create_user(self, data):
        return self.post(f"{self.url}/api/users", data)

    def put_user(self, data, id):
        return self.put(f"{self.url}/api/users/{id}", data)

    def patch_user(self, data, id):
        return self.patch(f"{self.url}/api/users/{id}", data)

    def delete_user(self, user_id):
        return self.delete(f"{self.url}/api/users/{user_id}")

    def register_user(self, data):
        return self.post(f"{self.url}/api/register", data)

    def login_user(self, data):
        return self.post(f"{self.url}/api/login", data)

    def get_delay(self, delay):
        return self.get(f"{self.url}/api/users?delay={delay}")
