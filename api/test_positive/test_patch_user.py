import pytest

from data.data_users import records


class TestReqresPatchUsers:
    @pytest.mark.positive
    @pytest.mark.parametrize('record', records, ids=[str(record['id']) for record in records])
    def test_patch_user(self, api, record):
        user_data = {
            "email": record['email'],
            "first_name": record['first_name'],
            "last_name": record['last_name'],
            "avatar": record['avatar']
        }
        response_create = api.create_user(user_data)
        data_create = response_create.json()

        new_user_data = {
            "first_name": "new_name",
        }
        response = api.patch_user(data_create['id'], new_user_data)
        data = response.json()
        assert response.status_code == 200
        assert 'updatedAt' in data
