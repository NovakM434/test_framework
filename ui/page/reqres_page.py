import json
from typing import KeysView
from page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.common.by import By

class ReqresPage(BasePage):
    path = '/'

    def __init__(self, driver):
        super().__init__(driver)

    def get_tagline_text(self):
        tagline_element = self._find_element(By.CLASS_NAME, 'tagline')
        return tagline_element.text

    def get_users_list(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="users"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        users_data = json.loads(data_json)
        users_list_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="users"]')
        users_list_link_element = users_list_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = users_list_link_element.get_attribute('href')
        return users_data, api_end_point

    def get_user_data(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="users-single"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        user_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="users-single"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return user_data, api_end_point

    def get_user_not_found(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="users-single-not-found"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        user_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="users-single-not-found"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return user_data, api_end_point

    def get_list_resource(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="unknown"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="unknown"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def not_found_resource(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="unknown-single-not-found"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="unknown-single-not-found"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def create_user(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="post"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="post"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def put_user(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="put"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="put"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def patch_user(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="patch"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="patch"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def delete_user(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="delete"] a[data-key="try-link"]')
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="delete"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return api_end_point

    def register_successful(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="register-successful"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="register-successful"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def register_unsuccessful(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="register-unsuccessful"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="register-unsuccessful"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def login_successful(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="login-successful"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="login-successful"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def login_unsuccessful(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="login-unsuccessful"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="login-unsuccessful"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point

    def delay(self):
        self._click(By.CSS_SELECTOR, 'li[data-id="delay"] a[data-key="try-link"]')
        pre_element = self._find_element(By.CSS_SELECTOR, 'pre[data-key="output-response"]')
        data_json = pre_element.text
        list_resource_data = json.loads(data_json)
        page_button_element = self._find_element(By.CSS_SELECTOR, 'li[data-id="delay"]')
        page_button_link_element = page_button_element.find_element(By.CSS_SELECTOR, 'a[data-key="try-link"]')
        api_end_point = page_button_link_element.get_attribute('href')
        return list_resource_data, api_end_point
