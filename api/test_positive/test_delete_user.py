import pytest


class TestReqresUserDelete:

    @pytest.mark.positive
    @pytest.mark.parametrize('user_id', [1, 2])
    def test_user_delete(self, api, user_id):
        response = api.delete_user(user_id)
        assert response.status_code == 204
