# from django.test import TestCase
from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class LoginFormTest(LiveServerTestCase):

    def setUp(self) -> None:
        User = get_user_model()
        User.objects.create_user(
            username='test_username',
            password='test_password',
            user_type=User.UserTypes.STUDENT
        )
        User.objects.create_superuser(
            username='test_admin',
            password='test_admin_password',
            user_type=User.UserTypes.STUDENT
        )

        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
        
    # def test_login_form(self):
     
    #     self.driver.get(self.live_server_url)
    #     self.driver.implicitly_wait(15)

    #     username = self.driver.find_element_by_name('username')
    #     password = self.driver.find_element_by_name('password')
    #     submit = self.driver.find_element_by_name('submit')

    #     username.send_keys('test_username')
    #     password.send_keys('test_password')
    #     submit.send_keys(Keys.RETURN)

    #     assert 'test_username' in self.driver.page_source

    def test_admin_page_login(self):
        self.driver.get(self.live_server_url)
        self.driver.implicitly_wait(15)

        self.driver.find_element_by_link_text('admin').click()
        # sleep(10)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

        username.send_keys('test_admin')
        password.send_keys('test_admin_password')
        submit.send_keys(Keys.RETURN)

        # sleep(10)
        # ele = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.link_text, "Courses"))
        # )
        assert 'test_admin' in self.driver.page_source

