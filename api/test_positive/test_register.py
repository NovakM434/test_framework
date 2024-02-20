from utils.api_method import ReqresApi
from utils.api_base import Api

import pytest

class TestReqresRegister:

    @pytest.mark.positive
    @pytest.mark.parametrize('email,password',
                             [("eve.holt@reqres.in", "pistol"),
                              ("emma.wong@reqres.in", "luperkal")])
    def test_register_successful(self, api, email, password):
        post_data = {
            "email": email,
            "password" : password
        }
        response = api.register_user(post_data)
        data = response.json()
        print(response.status_code)
        print(data)
        assert response.status_code == 200
        assert 'id' in data
        assert 'token' in data
