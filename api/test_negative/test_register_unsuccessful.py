import pytest


class TestRegisterUnSuccessful:

    @pytest.mark.negative
    @pytest.mark.parametrize('email,username', [('cat@mail.ru', '')])
    def test_login_unsuccesful(self, api, email, username):
        data_login = {
            'email': email,
            'username': username
        }
        response = api.register_user(data_login)
        data = response.json()
        assert response.status_code == 400
        assert "Missing password" in data['error']
