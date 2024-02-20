import pytest


class TestReqresSingleUserPage:

    @pytest.mark.positive
    @pytest.mark.parametrize('user_id', [1, 2])
    def test_get_single_user_valid(self, api, user_id):
        response = api.get_single_user(user_id)
        data = response.json()
        assert response.status_code == 200
        assert len(response.json()['data']) > 0
        assert data['data']['id'] == user_id
        assert all(key in data['data'] for key in ['email', 'id', 'first_name', 'last_name'])
