import time
import pytest


class TestReqresDelay:

    @pytest.mark.positive
    @pytest.mark.parametrize('delay', [3, 4])
    def test_delay(self, api, delay):
        start_time = time.time()
        response = api.get_delay(delay)
        end_time = time.time()
        response_time = end_time - start_time
        assert response_time >= delay
        assert response.status_code == 200
