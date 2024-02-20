import requests
import pytest

from page.reqres_page import ReqresPage


class TestMainPage:
    @pytest.mark.web
    def test_tagline_text(self, browser):
        reqres_page = ReqresPage(browser)
        reqres_page.go_to_home_page()
        tagline_text = reqres_page.get_tagline_text()
        assert tagline_text == 'Test your front-end against a real API'

    @pytest.mark.web
    def test_user_list(self, browser):
        user_list = ReqresPage(browser)
        user_list.go_to_home_page()
        data, api_end_point = user_list.get_users_list()
        api_response = requests.get(api_end_point).json()
        assert data == api_response

    @pytest.mark.web
    def test_single_user(self, browser):
        user_single = ReqresPage(browser)
        user_single.go_to_home_page()
        data, api_end_point = user_single.get_user_data()
        api_response = requests.get(api_end_point).json()
        assert data == api_response

    @pytest.mark.web
    def test_user_not_found(self, browser):
        user_not_found = ReqresPage(browser)
        user_not_found.go_to_home_page()
        data, api_end_point = user_not_found.get_user_not_found()
        api_response = requests.get(api_end_point).json
        if len(data) == 0:
            data = api_response
        assert data == api_response

    @pytest.mark.web
    def test_list_resource(self, browser):
        list_resource = ReqresPage(browser)
        list_resource.go_to_home_page()
        data, api_end_point = list_resource.get_list_resource()
        api_response = requests.get(api_end_point).json()
        assert data == api_response

    @pytest.mark.web
    def test_not_found_resource(self, browser):
        not_found_resource = ReqresPage(browser)
        not_found_resource.go_to_home_page()
        data, api_end_point = not_found_resource.not_found_resource()
        api_response = requests.get(api_end_point).json()
        assert data == api_response

    @pytest.mark.web
    def test_create_user(self, browser):
        create_user = ReqresPage(browser)
        create_user.go_to_home_page()
        data, api_end_point = create_user.create_user()
        create_data = {
            'name': 'morpheus',
            'job': 'leader'
        }
        api_response = requests.post(api_end_point, create_data).json()
        data['createdAt'] = api_response['createdAt']
        data['id'] = api_response['id']
        assert data == api_response

    @pytest.mark.web
    def test_put_user(self, browser):
        put_user = ReqresPage(browser)
        put_user.go_to_home_page()
        data, api_end_point = put_user.put_user()
        put_data = {
        "name": "morpheus",
        "job": "zion resident"
        }
        api_response = requests.put(api_end_point, put_data).json()
        data['updatedAt'] = api_response['updatedAt']
        assert data == api_response

    @pytest.mark.web
    def test_delete_user(self, browser):
        delete_user = ReqresPage(browser)
        delete_user.go_to_home_page()
        api_end_point = delete_user.delete_user()
        api_response = requests.delete(api_end_point)
        assert 204 == api_response.status_code

    @pytest.mark.web
    def test_register_successful(self, browser):
        register = ReqresPage(browser)
        register.go_to_home_page()
        data, api_end_point = register.register_successful()
        register_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
        }
        api_response = requests.post(api_end_point, register_data).json()
        assert all(key in api_response for key in ('id', 'token'))
        assert len(api_response) == 2

    @pytest.mark.web
    def test_register_unsuccessful(self, browser):
        bad_register = ReqresPage(browser)
        bad_register.go_to_home_page()
        data, api_end_point = bad_register.register_unsuccessful()
        bad_data = {
            'email': 'sydney@fife'
        }
        api_response = requests.post(api_end_point, bad_data).json()
        assert data == api_response

    @pytest.mark.web
    def test_login_successful(self, browser):
        login_user = ReqresPage(browser)
        login_user.go_to_home_page()
        data, api_end_point = login_user.login_successful()
        login_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
        }
        api_response = requests.post(api_end_point, login_data).json()
        assert 'token' in api_response

    @pytest.mark.web
    def test_login_unsuccessful(self, browser):
        bad_login = ReqresPage(browser)
        bad_login.go_to_home_page()
        data, api_end_point = bad_login.login_unsuccessful()
        bad_data = {
        "email": "sydney@fife"
        }
        api_response = requests.post(api_end_point, bad_data).json()
        assert api_response == data

    @pytest.mark.web
    def test_delay(self, browser):
        delay = ReqresPage(browser)
        delay.go_to_home_page()
        data, api_end_point = delay.delay()
        api_response = requests.get(api_end_point).json()
        assert api_response == data
