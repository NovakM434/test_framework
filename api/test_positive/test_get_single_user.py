from utils.api_method import ReqresApi
from utils.api_base import Api

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


    # @pytest.mark.parametrize('user_id', ["one", "two", -1, [], 23])
    # def test_get_single_user_not_valid(self, api, user_id):
    #     single_user_page = RegresSingleUserPage(api, user_id)
    #     response = single_user_page.get_single_user()
    #     assert response.status_code == 404
