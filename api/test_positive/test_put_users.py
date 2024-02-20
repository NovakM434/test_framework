import pytest

from data.data_users import records


class TestReqresPutUsers:

    @pytest.mark.positive
    @pytest.mark.parametrize('record', records, ids=[str(record['id']) for record in records])
    def test_put_users(self, api, record):
        user_data = {
            "email": record['email'],
            "first_name": record['first_name'],
            "last_name": record['last_name'],
            "avatar": record['avatar']
        }
        response_create = api.create_user(user_data)
        data_create = response_create.json()
        new_user_data = {
            "email": "new_email",
            "first_name": "new_name",
            "last_name": "new_last_name",
            "avatar": "new_avatar"
        }
        response = api.put_user(data_create['id'], new_user_data)
        data = response.json()
        assert response.status_code == 200
        assert 'updatedAt' in data
