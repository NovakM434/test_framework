import pytest


class TestReqresLogin:

    @pytest.mark.positive
    @pytest.mark.parametrize('email,password',
                             [("eve.holt@reqres.in", "pistol"),
                              ("emma.wong@reqres.in", "luperkal")])
    def test_login_successful(self, api, email, password):
        post_data = {
            "email": email,
            "password" : password
        }
        response = api.login_user(post_data)
        data = response.json()
        print(response.status_code)
        print(data)
        assert response.status_code == 200
        assert 'token' in data
