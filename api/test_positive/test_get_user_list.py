import pytest


class TestRegresUserList:

    @pytest.mark.positive
    @pytest.mark.parametrize('page_id', [1, 2])
    def test_get_user_list_valid(self, api, page_id):
        response = api.get_list_user(page_id)
        data = response.json()
        print(data)
        assert data['page'] == page_id
        assert len(data['data']) == 6
        assert response.status_code == 200
        assert len(data) > 0
        assert all(key in data['data'][0] for key in ['email', 'id', 'first_name', 'last_name'])
