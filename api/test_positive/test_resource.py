import pytest


class TestReqresResource:

    @pytest.mark.positive
    def test_get_resource_list(self, api):
        response = api.get_resource_list()
        data = response.json()
        assert len(data['data']) == 6
        assert response.status_code == 200
        assert len(data) > 0
        assert all(key in data['data'][0] for key in ['name', 'id', 'color', 'pantone_value'])

    @pytest.mark.positive
    @pytest.mark.parametrize('resource_id', [1, 2])
    def test_get_resource_single(self, api, resource_id):
        response = api.get_resource_single(resource_id)
        data = response.json()
        assert response.status_code == 200
        assert data['data']['id'] == resource_id
        assert len(data) > 0
        assert all(key in data['data'] for key in ['name', 'id', 'color', 'pantone_value'])
