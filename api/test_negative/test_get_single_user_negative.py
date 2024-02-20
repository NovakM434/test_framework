import pytest


class TestReqresSingleUserPageNegative:

    @pytest.mark.negative
    @pytest.mark.parametrize('user_id', ["one", -1, [], 23])
    def test_get_single_user_not_valid(self, api, user_id):
        response = api.get_single_user(user_id)
        assert response.status_code == 404
