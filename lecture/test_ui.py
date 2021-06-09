# # from django.test import TestCase
# from time import sleep

# from django.contrib.auth import get_user_model
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# LOCAL_SITE_URL = 'http://localhost:8000/'

# class AddFormTest(LiveServerTestCase):
#     def setUp(self) -> None:
#         User = get_user_model()
#         User.objects.create_user(
#             username="test_username",
#             password="test_password",
#             user_type=User.UserTypes.STUDENT,
#         )
#         User.objects.create_superuser(
#             username="admin",
#             password="password",
#             user_type=User.UserTypes.STUDENT,
#         )
#         options = webdriver.ChromeOptions()
#         options.add_argument("--ignore-certificate-error")
#         options.add_argument("--ignore-ssl-errors")
#         options.add_experimental_option("excludeSwitches", ["enable-logging"])

#         self.driver = webdriver.Chrome(options=options)
#         self.driver.maximize_window()

#     def tearDown(self) -> None:
#         self.driver.refresh()
#         self.driver.close()

#     def test_add_department(self):
    
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(15)
#         self.driver.get(self.live_server_url + "/admin/")
#         # self.driver.get('http://localhost:8000/admin/')


#         username = self.driver.find_element_by_name('username')
#         password = self.driver.find_element_by_name('password')
#         submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#         username.send_keys('admin')
#         password.send_keys('password')
#         submit.send_keys(Keys.RETURN)

#         submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[1]/a')
#         submit.send_keys(Keys.RETURN)

#         dept_code = self.driver.find_element_by_name('dept_code')
#         dept_name = self.driver.find_element_by_name('dept_name')
#         submit = self.driver.find_element_by_name('_save')

#         dept_code.send_keys('ECE')
#         dept_name.send_keys('electrical communication')
#         submit.send_keys(Keys.RETURN)
#         assert 'electrical communication' in self.driver.page_source

#     # def test_add_applications(self):
#     #     self.driver = webdriver.Chrome()
#     #     self.driver.get('http://localhost:8000/admin/')
#     #     self.driver.implicitly_wait(15)

#     #     username = self.driver.find_element_by_name('username')
#     #     password = self.driver.find_element_by_name('password')
#     #     submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     #     username.send_keys('admin')
#     #     password.send_keys('password')
#     #     submit.send_keys(Keys.RETURN)

#     #     self.driver.get('http://localhost:8000/admin/lecture/')
#     #     submit = self.driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[1]/td/a')
#     #     submit.send_keys(Keys.RETURN)
#     #     assert 'applications' in self.driver.page_source

#     # def test_add_cirfacultys(self):
        
#     #      self.driver = webdriver.Chrome()
#     #      self.driver.get('http://localhost:8000/admin/')

#     #      username = self.driver.find_element_by_name('username')
#     #      password = self.driver.find_element_by_name('password')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     #      username.send_keys('admin')
#     #      password.send_keys('password')
#     #      submit.send_keys(Keys.RETURN)

#     #      self.driver.get('http://localhost:8000/admin/lecture/')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[2]/td/a')
#     #      submit.send_keys(Keys.RETURN)
#     #      assert 'faculty' in self.driver.page_source
        
#     # def test_add_events(self):
        
#     #      self.driver = webdriver.Chrome()
#     #      self.driver.get('http://localhost:8000/admin/')

#     #      username = self.driver.find_element_by_name('username')
#     #      password = self.driver.find_element_by_name('password')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     #      username.send_keys('admin')
#     #      password.send_keys('password')
#     #      submit.send_keys(Keys.RETURN)

#     #      self.driver.get('http://localhost:8000/admin/lecture/')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/nav/div[3]/table/tbody/tr[4]/td/a')
#     #      submit.send_keys(Keys.RETURN)
#     #      assert 'Add event' in self.driver.page_source

#     # def test_add_externalusers(self):
        
#     #      self.driver = webdriver.Chrome()
#     #      self.driver.get('http://localhost:8000/admin/')

#     #      username = self.driver.find_element_by_name('username')
#     #      password = self.driver.find_element_by_name('password')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     #      username.send_keys('admin')
#     #      password.send_keys('password')
#     #      submit.send_keys(Keys.RETURN)

#     #      self.driver.get('http://localhost:8000/admin/lecture/')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[5]/td/a')
#     #      submit.send_keys(Keys.RETURN)
#     #      assert 'Add external user' in self.driver.page_source
        
#     # def test_add_facultys(self):
        
#     #      self.driver = webdriver.Chrome()
#     #      self.driver.get('http://localhost:8000/admin/')

#     #      username = self.driver.find_element_by_name('username')
#     #      password = self.driver.find_element_by_name('password')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     #      username.send_keys('admin')
#     #      password.send_keys('password')
#     #      submit.send_keys(Keys.RETURN)

#     #      self.driver.get('http://localhost:8000/admin/lecture/')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[6]/td/a')
#     #      submit.send_keys(Keys.RETURN)
#     #      assert 'faculty' in self.driver.page_source

#     # def test_add_guests(self):
        
#     #      self.driver = webdriver.Chrome()
#     #      self.driver.get('http://localhost:8000/admin/')

#     #      username = self.driver.find_element_by_name('username')
#     #      password = self.driver.find_element_by_name('password')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     #      username.send_keys('admin')
#     #      password.send_keys('password')
#     #      submit.send_keys(Keys.RETURN)

#     #      self.driver.get('http://localhost:8000/admin/lecture/')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[7]/td/a')
#     #      submit.send_keys(Keys.RETURN)
#     #      assert 'guest' in self.driver.page_source

#     # def test_add_students(self):
        
#     #      self.driver = webdriver.Chrome()
#     #      self.driver.get('http://localhost:8000/admin/')

#     #      username = self.driver.find_element_by_name('username')
#     #      password = self.driver.find_element_by_name('password')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     #      username.send_keys('admin')
#     #      password.send_keys('password')
#     #      submit.send_keys(Keys.RETURN)

#     #      # self.driver.get('http://localhost:8000/admin/lecture/')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[8]/td/a')
#     #      submit.send_keys(Keys.RETURN)
#     #      assert 'student' in self.driver.page_source

#     # def test_admin_page_logout(self):

#     #      self.driver = webdriver.Chrome()
#     #      self.driver.get('http://localhost:8000/admin/')

#     #      username = self.driver.find_element_by_name('username')
#     #      password = self.driver.find_element_by_name('password')
#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     #      username.send_keys('admin')
#     #      password.send_keys('password')
#     #      submit.send_keys(Keys.RETURN)

#     #      submit = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[3]')
#     #      submit.send_keys(Keys.RETURN)

#     #      assert 'logout' in self.driver.page_source



# # from django.contrib.auth.models import Group, Permission
# # cir_faculty_group, created = Group.objects.create(name='CIRFacultyGroup')
# # faculty_group, created = Group.objects.create(name='FacultyGroup')
