# # from django.test import TestCase
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# LOCAL_SITE_URL = 'http://127.0.0.1:8000/'

# class LoginFormTest(LiveServerTestCase):

#   def test_add_department(self):
    
#     driver = webdriver.Chrome()
#     driver.get('http://localhost:8000/admin/')

#     username = driver.find_element_by_name('username')
#     password = driver.find_element_by_name('password')
#     submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#     username.send_keys('admin')
#     password.send_keys('password')
#     submit.send_keys(Keys.RETURN)

#     submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[1]/a')
#     submit.send_keys(Keys.RETURN)

#     # dept_code = driver.find_element_by_name('username')
#     # password = driver.find_element_by_name('password')


#     # assert 'department' in driver.page_source
    
#     # driver.get('http://localhost:8000/admin/lecture/department/add/')
#     dept_code = driver.find_element_by_name('dept_code')
#     dept_name = driver.find_element_by_name('dept_name')
#     submit = driver.find_element_by_name('_save')

#     dept_code.send_keys('ECE')
#     dept_name.send_keys('electrical communication')
#     submit.send_keys(Keys.RETURN)
#     assert 'electrical communication' in driver.page_source

#   def test_add_applications(self):
#      driver = webdriver.Chrome()
#      driver.get('http://localhost:8000/admin/')

#      username = driver.find_element_by_name('username')
#      password = driver.find_element_by_name('password')
#      submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#      username.send_keys('admin')
#      password.send_keys('password')
#      submit.send_keys(Keys.RETURN)

#      driver.get('http://localhost:8000/admin/lecture/')
#      submit = driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[1]/td/a')
#      submit.send_keys(Keys.RETURN)
#      assert 'applications' in driver.page_source

#   def test_add_cirfacultys(self):
       
#      driver = webdriver.Chrome()
#      driver.get('http://localhost:8000/admin/')

#      username = driver.find_element_by_name('username')
#      password = driver.find_element_by_name('password')
#      submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#      username.send_keys('admin')
#      password.send_keys('password')
#      submit.send_keys(Keys.RETURN)

#      driver.get('http://localhost:8000/admin/lecture/')
#      submit = driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[2]/td/a')
#      submit.send_keys(Keys.RETURN)
#      assert 'faculty' in driver.page_source
    
#   def test_add_events(self):
       
#      driver = webdriver.Chrome()
#      driver.get('http://localhost:8000/admin/')

#      username = driver.find_element_by_name('username')
#      password = driver.find_element_by_name('password')
#      submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#      username.send_keys('admin')
#      password.send_keys('password')
#      submit.send_keys(Keys.RETURN)

#      driver.get('http://localhost:8000/admin/lecture/')
#      submit = driver.find_element_by_xpath('/html/body/div[1]/div[3]/nav/div[3]/table/tbody/tr[4]/td/a')
#      submit.send_keys(Keys.RETURN)
#      assert 'Add event' in driver.page_source

#   def test_add_externalusers(self):
       
#      driver = webdriver.Chrome()
#      driver.get('http://localhost:8000/admin/')

#      username = driver.find_element_by_name('username')
#      password = driver.find_element_by_name('password')
#      submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#      username.send_keys('admin')
#      password.send_keys('password')
#      submit.send_keys(Keys.RETURN)

#      driver.get('http://localhost:8000/admin/lecture/')
#      submit = driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[5]/td/a')
#      submit.send_keys(Keys.RETURN)
#      assert 'Add external user' in driver.page_source
    
#   def test_add_facultys(self):
       
#      driver = webdriver.Chrome()
#      driver.get('http://localhost:8000/admin/')

#      username = driver.find_element_by_name('username')
#      password = driver.find_element_by_name('password')
#      submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#      username.send_keys('admin')
#      password.send_keys('password')
#      submit.send_keys(Keys.RETURN)

#      driver.get('http://localhost:8000/admin/lecture/')
#      submit = driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[6]/td/a')
#      submit.send_keys(Keys.RETURN)
#      assert 'faculty' in driver.page_source

#   def test_add_guests(self):
       
#      driver = webdriver.Chrome()
#      driver.get('http://localhost:8000/admin/')

#      username = driver.find_element_by_name('username')
#      password = driver.find_element_by_name('password')
#      submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#      username.send_keys('admin')
#      password.send_keys('password')
#      submit.send_keys(Keys.RETURN)

#      driver.get('http://localhost:8000/admin/lecture/')
#      submit = driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[7]/td/a')
#      submit.send_keys(Keys.RETURN)
#      assert 'guest' in driver.page_source

#   def test_add_students(self):
       
#      driver = webdriver.Chrome()
#      driver.get('http://localhost:8000/admin/')

#      username = driver.find_element_by_name('username')
#      password = driver.find_element_by_name('password')
#      submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#      username.send_keys('admin')
#      password.send_keys('password')
#      submit.send_keys(Keys.RETURN)

#      # driver.get('http://localhost:8000/admin/lecture/')
#      submit = driver.find_element_by_xpath('/html/body/div/div[3]/nav/div[3]/table/tbody/tr[8]/td/a')
#      submit.send_keys(Keys.RETURN)
#      assert 'student' in driver.page_source

#   def test_admin_page_logout(self):

#      driver = webdriver.Chrome()
#      driver.get('http://localhost:8000/admin/')

#      username = driver.find_element_by_name('username')
#      password = driver.find_element_by_name('password')
#      submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

#      username.send_keys('admin')
#      password.send_keys('password')
#      submit.send_keys(Keys.RETURN)

#      submit = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[3]')
#      submit.send_keys(Keys.RETURN)

#      assert 'logout' in driver.page_source

