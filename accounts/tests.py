# from django.test import TestCase


from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PlayerFormTest(LiveServerTestCase):

  def test_login_form(self):
    selenium = webdriver.Chrome()
    
    selenium.get('http://127.0.0.1:8000/')
    
    username = selenium.find_element_by_name('username')
    password = selenium.find_element_by_name('password')

    submit = selenium.find_element_by_name('submit')

    username.send_keys('test_username')
    password.send_keys('test_password')

    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'test_username' in selenium.page_source