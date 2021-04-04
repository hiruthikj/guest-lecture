# from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LOCAL_SITE_URL = 'http://127.0.0.1:8000/'

class LoginFormTest(LiveServerTestCase):

  def test_login_form(self):
    driver = webdriver.Chrome()
    driver.get(LOCAL_SITE_URL)
    
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    submit = driver.find_element_by_name('submit')

    username.send_keys('test_username')
    password.send_keys('test_password')
    submit.send_keys(Keys.RETURN)

    assert 'test_username' in driver.page_source
