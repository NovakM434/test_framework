from utils.api_method import ReqresApi
from utils.api_base import Api

import pytest

class TestReqresResourceNegative:

    @pytest.mark.negative
    @pytest.mark.parametrize('resource_id', [23, 32, 'two'])
    def test_get_resource_not_found(self, api, resource_id):
        response = api.get_resource_single(resource_id)
        assert response.status_code == 404
