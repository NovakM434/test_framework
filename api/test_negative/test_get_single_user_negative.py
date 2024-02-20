from utils.api_method import ReqresApi
from utils.api_base import Api

import pytest


class TestReqresSingleUserPageNegative:

    @pytest.mark.negative
    @pytest.mark.parametrize('user_id', ["one", "two", -1, [], 23])
    def test_get_single_user_not_valid(self, api, user_id):
        response = api.get_single_user(user_id)
        assert response.status_code == 404
