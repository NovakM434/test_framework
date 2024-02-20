import pytest

from data.data_users import records


class TestReqresCreateUser:

    @pytest.mark.positive
    @pytest.mark.parametrize('record', records, ids=[str(record['id']) for record in records])
    def test_create_user(self, api, record):
        user_data = {
            "email": record['email'],
            "first_name": record['first_name'],
            "last_name": record['last_name'],
            "avatar": record['avatar']
        }
        response = api.create_user(user_data)
        data = response.json()

        assert response.status_code == 201
        assert data['first_name'] == record['first_name']
        assert data['last_name'] == record['last_name']
        assert 'id' in data
        assert 'createdAt' in data
