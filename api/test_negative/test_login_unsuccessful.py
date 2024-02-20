from utils.api_method import ReqresApi
from utils.api_base import Api

import pytest

class TestLoginUnSuccessful:

    @pytest.mark.negative
    @pytest.mark.parametrize('email,username', [('cat@mail.ru', ''), ('meow@mail.ru', '')])
    def test_login_unsuccesful(self, api, email, username):
        data_login = {
            'email': email,
            'username': username
        }
        response = api.login_user(data_login)
        data = response.json()
        assert response.status_code == 400
        assert "Missing password" in data['error']
