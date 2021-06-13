from django.utils.translation import deactivate
import accounts
from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from lecture.models import Guest, Faculty, CIRFaculty, Student,Department
from django.contrib.auth.models import Group, Permission
from lecture.models import Student, Event ,Department


class LoginFormTest(LiveServerTestCase):
    def setUp(self) -> None:
        User = get_user_model()
        User.objects.create_user(
            username="test_username",
            password="test_password",
            user_type=User.UserTypes.STUDENT,
        )
        User.objects.create_superuser(
            username="test_admin",
            password="test_admin_password",
            user_type=User.UserTypes.STUDENT,
        )

        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        # self.addCleanup(self.driver.quit)

    def tearDown(self) -> None:
        self.driver.refresh()
        self.driver.close()

    def test_login_logout(self):
        self.driver.get(self.live_server_url)
        self.driver.implicitly_wait(15)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_name('submit')

        username.send_keys('test_username')
        password.send_keys('test_password')
        submit.send_keys(Keys.RETURN)
        sleep(2)

        main_logout = self.driver.find_element_by_xpath("/html/body/nav/div/div/div[3]/a")
        main_logout.send_keys(Keys.RETURN)
        
        sleep(2)
        main_loginagain = self.driver.find_element_by_xpath("/html/body/div/div/a/button")
        main_loginagain.send_keys(Keys.RETURN)
        sleep(2)
        assert 'LECTURE SYSTEM' in self.driver.page_source

    def test_admin_page_login_logout(self):
        self.driver.get(self.live_server_url)
        self.driver.implicitly_wait(15)

        v = self.driver.find_element_by_xpath("/html/body/div/div/span/a")
        v.send_keys(Keys.RETURN)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

        username.send_keys('test_admin')
        password.send_keys('test_admin_password')
        submit.send_keys(Keys.RETURN)
        sleep(2)

        admin_logout  = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[3]")
        admin_logout.send_keys(Keys.RETURN)

        sleep(2)
        admin_loginagain = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/p[2]/a")
        admin_loginagain.send_keys(Keys.RETURN)
        sleep(2)
        assert 'Event Administration' in self.driver.page_source


class EventTest(LiveServerTestCase):
    def setUp(self) -> None:
        User = get_user_model()
        # User.objects.create_user(
        #     username="test_username",
        #     password="test_password",
        #     user_type=User.UserTypes.STUDENT,
        # )
        User.objects.create_superuser(
            username="test_admin",
            password="test_admin_password",
            user_type=User.UserTypes.STUDENT,
        )
        stud_acc = User.objects.create_user(
            username="test_stud",
            password="test_fac_password",
            email="aa@gmail.com",
            user_type=User.UserTypes.STUDENT,
        )
        dept = Department.objects.create(
            dept_code = "CSE",
            dept_name = "Computer Science Engineering"
        )
        student = Student.objects.create(
            account=stud_acc,
            dept_fk=dept,
            reg_no="CSE18888"
        )
        guest_acc = User.objects.create_user(
            username="test_guest1",
            password="test_guest_password1",
            user_type=User.UserTypes.GUEST,
        )
        guest = Guest.objects.create(
            account = guest_acc,
            details = "test_details"
        )
        event = Event.objects.create(
            event_name = "test_event_name",
            start_date = "2021-10-25 14:30:59+0530",
            end_date = "2021-10-27 14:30:59+0530",
            max_seats = 21,
            occupied_seats = 1,
            guest_fk = guest,
            allow_ext = True,
            description = "description",
            summary = "summary",
            place = "place",
        )

        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.refresh()
        self.driver.close()

    def test_upcomingevents(self):
        self.driver.get(self.live_server_url)
        self.driver.implicitly_wait(15)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_name('submit')

        username.send_keys('test_stud')
        password.send_keys('test_fac_password')
        submit.send_keys(Keys.RETURN)

        sleep(1)
        test_upcoming = self.driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/ul/li[2]/p/a")
        test_upcoming.send_keys(Keys.RETURN)

        sleep(1)
        up_link = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/a")
        up_link.send_keys(Keys.RETURN)

        sleep(1) 
        up_register = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/form/button")
        up_register.click()
        sleep(1)

        return_up = self.driver.find_element_by_xpath("/html/body/nav/div/div/div[1]/a[1]")
        return_up.send_keys(Keys.RETURN)
        
        sleep(1)
        test_applied = self.driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/ul/li[1]/p/a")
        test_applied.send_keys(Keys.RETURN)
        sleep(1)
        up_link = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/a")
        up_link.send_keys(Keys.RETURN)
        sleep(1)



    def test_appliedevents(self):
        self.driver.get(self.live_server_url)
        self.driver.implicitly_wait(15)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_name('submit')

        username.send_keys('test_stud')
        password.send_keys('test_fac_password')
        submit.send_keys(Keys.RETURN)

        sleep(1)
        test_applied = self.driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/ul/li[1]/p/a")
        test_applied.send_keys(Keys.RETURN)
        sleep(1)


    def test_pastevents(self):
        self.driver.get(self.live_server_url)
        self.driver.implicitly_wait(15)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_name('submit')

        username.send_keys('test_stud')
        password.send_keys('test_fac_password')
        submit.send_keys(Keys.RETURN)

        sleep(1)
        test_past = self.driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/ul/li[3]/p/a")
        test_past.send_keys(Keys.RETURN)
        sleep(1)
       
class AdminSiteTest(LiveServerTestCase):
    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

        User = get_user_model()
        User.objects.create_user(
            username="test_username",
            password="test_password",
            user_type=User.UserTypes.STUDENT,
        )
        User.objects.create_superuser(
            username="test_admin",
            password="test_admin_password",
            user_type=User.UserTypes.STUDENT,
        )
        guest_acc = User.objects.create(
            username="test_guest",
            password="test_guest_password",
            user_type=User.UserTypes.GUEST,
        )
        guest1_acc = User.objects.create(
            username="test_guest1",
            password="test_guest_password1",
            user_type=User.UserTypes.GUEST,
        )
        fac_acc = User.objects.create(
            username="test_fac",
            password="test_fac_password",
            user_type=User.UserTypes.FACULTY,
        )
        cir_fac_acc = User.objects.create(
            username="test_cir_fac",
            password="test_fac_password",
            user_type=User.UserTypes.CIR_FACULTY,
        )
        stud_acc = User.objects.create(
            username="test_stud",
            password="test_fac_password",
            user_type=User.UserTypes.STUDENT,
        )
        ext_acc = User.objects.create(
            username="ext_stud",
            password="test_fac_password",
            user_type=User.UserTypes.OTHERS,
        )
        Guest.objects.create(
            account = guest_acc,
            details = "test_details"
        )
        Department.objects.create(
            dept_code = "CSE",
            dept_name = "Computer Science Engineering"
        )
        cir_faculty_group= Group.objects.create(name='CIRFacultyGroup')
        faculty_group = Group.objects.create(name='FacultyGroup')

    def tearDown(self) -> None:
        self.driver.close()

    def test_user(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)
        # ---------------------------------------------USER------------------------------------------------------
        sleep(1)
        users = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr/th/a"
        )
        users.send_keys(Keys.RETURN)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        sleep(1)
        self.driver.get(self.live_server_url + "/admin/")
        # --------------------------------------------USER_ADD----------------------------------------------------
        sleep(1)
        user_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr/td[1]/a"
        )
        user_add.send_keys(Keys.RETURN)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password1")
        password_conformation = self.driver.find_element_by_name("password2")
        user_type = self.driver.find_element_by_name("user_type")
        phonenumber = self.driver.find_element_by_name("phone_no")
        save = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]"
        )

        sleep(1)
        username.send_keys("s1")
        password.send_keys("student@#$1")
        password_conformation.send_keys("student@#$1")
        user_type.send_keys("student")
        phonenumber.send_keys("6302456778")
        save.send_keys(Keys.RETURN)
        sleep(1)

        first_name = self.driver.find_element_by_name("first_name")
        last_name = self.driver.find_element_by_name("last_name")
        email_address = self.driver.find_element_by_name("email")
        save = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]"
        )

        sleep(3)
        first_name.send_keys("student")
        last_name.send_keys("1")
        email_address.send_keys("student1@gmail.com")
        save.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # -------------------------------------------USER_CHANGE---------------------------------------------------------------
        user_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr/td[2]/a"
        )
        user_change.send_keys(Keys.RETURN)
        sleep(1)

        block = self.driver.find_element_by_name("q")
        search = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/form/div/input[2]"
        )

        sleep(1)
        block.send_keys("s1")
        search.send_keys(Keys.RETURN)

        sleep(1)
        ac = self.driver.find_element_by_name("_selected_action")
        ac.click()

        sleep(1)
        action = self.driver.find_element_by_name("action")
        action.send_keys("Delete selected users")
        go = self.driver.find_element_by_name("index")
        go.send_keys(Keys.RETURN)

        sleep(1)
        takemeback = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        takemeback.send_keys(Keys.RETURN)
        go = self.driver.find_element_by_name("index")
        go.send_keys(Keys.RETURN)

        sleep(1)
        yes = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/input[4]"
        )
        yes.send_keys(Keys.RETURN)
        sleep(1)
    
    def test_groups(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)
        # ---------------------------------------------GROUPS------------------------------------------------------------------
        groups = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/th/a"
        )
        groups.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # --------------------------------------------GROUP_ADD------------------------------------------------------
        group_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/td[1]/a"
        )
        group_add.send_keys(Keys.RETURN)
        sleep(1)

        grp_name = self.driver.find_element_by_name("name")
        chooseall = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/div[1]/div/div[1]/a"
        )
        grp_save = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]"
        )

        sleep(1)
        grp_name.send_keys("CSE")
        chooseall.click()
        grp_save.send_keys(Keys.RETURN)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # ------------------------------------------GROUP_CHANGE------------------------------------------------------------
        group_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/td[2]/a"
        )
        group_change.send_keys(Keys.RETURN)
        sleep(1)

        grp_name = self.driver.find_element_by_name("q")
        grp_x = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/form/div/input[2]"
        )

        sleep(1)
        grp_name.send_keys("CSE")
        grp_x.send_keys(Keys.RETURN)

        sleep(1)
        grp_sa = self.driver.find_element_by_name("_selected_action")
        grp_sa.click()

        sleep(1)
        grp_action = self.driver.find_element_by_name("action")
        grp_action.send_keys("Delete selected users")
        grp_go = self.driver.find_element_by_name("index")
        grp_go.send_keys(Keys.RETURN)

        sleep(1)
        grp_takemeback = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        grp_takemeback.send_keys(Keys.RETURN)
        grp_go = self.driver.find_element_by_name("index")
        grp_go.send_keys(Keys.RETURN)

        sleep(1)
        grp_yes = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/input[4]"
        )
        grp_yes.send_keys(Keys.RETURN)
        sleep(1)

       
    def test_cirfaculty(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)   
        # -------------------------------------------CIR FACULTY------------------------------------------------------------
        cirfaculty = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/th/a"
        )
        cirfaculty.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # --------------------------------------------CIR FACULTY_ADD---------------------------------------------------------
        cirfaculty_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[1]/a"
        )
        cirfaculty_add.send_keys(Keys.RETURN)

        cir_account = self.driver.find_element_by_name("account")
        cir_account.send_keys("test_cir_fac")

        cir_save = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]")
        cir_save.send_keys(Keys.RETURN)
        
  
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # ------------------------------------------CIR FACULTY_CHANGE---------------------------------------------------------
        cirfaculty_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/a"
        )
        cirfaculty_change.send_keys(Keys.RETURN)
        sleep(3)

        cirfaculty_b = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[1]")
        cirfaculty_b.send_keys("test_cir_fac")
        sleep(1)

        cirfaculty_se = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[2]")
        cirfaculty_se.send_keys(Keys.RETURN)

        cirfaculty_box = self.driver.find_element_by_name("_selected_action")
        cirfaculty_box.click()
        
        cirfaculty_action = self.driver.find_element_by_name("action")
        cirfaculty_action.send_keys("Delete selected departments")

        cirfaculty_go = self.driver.find_element_by_name("index")
        cirfaculty_go.send_keys(Keys.RETURN)
        sleep(1)

        cirfaculty_no = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        cirfaculty_no.send_keys(Keys.RETURN)
        sleep(1)

        cirfaculty_go = self.driver.find_element_by_name("index")
        cirfaculty_go.send_keys(Keys.RETURN)
        sleep(1)

        cirfaculty_yes = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/div/input[4]")
        cirfaculty_yes.send_keys(Keys.RETURN)
        
        
    def test_departments(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)    
        # ------------------------------------------DEPARTMENTS------------------------------------------------------------
        departments = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/th/a"
        )
        departments.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # ------------------------------------------DEPARTMENTS_ADD---------------------------------------------------------
        departments_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[1]/a"
        )
        departments_add.send_keys(Keys.RETURN)
        sleep(1)

        dept_code = self.driver.find_element_by_name("dept_code")
        dept_name = self.driver.find_element_by_name("dept_name")
        dept_save = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]"
        )

        sleep(1)
        dept_code.send_keys("CSE")
        dept_name.send_keys("Computer Science Engineering")
        dept_save.send_keys(Keys.RETURN)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # -------------------------------------------DEPARTMENT_CHANGE-----------------------------------------------
        department_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[2]/a"
        )
        department_change.send_keys(Keys.RETURN)

        dept_b = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[1]")
        dept_b.send_keys("Computer Science Engineering")
        sleep(1)

        dept_se = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[2]")
        dept_se.send_keys(Keys.RETURN)

        dept_box = self.driver.find_element_by_name("_selected_action")
        dept_box.click()
        
        dept_action = self.driver.find_element_by_name("action")
        dept_action.send_keys("Delete selected departments")

        dept_go = self.driver.find_element_by_name("index")
        dept_go.send_keys(Keys.RETURN)
        sleep(1)

        dept_no = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        dept_no.send_keys(Keys.RETURN)
        sleep(1)

        dept_go = self.driver.find_element_by_name("index")
        dept_go.send_keys(Keys.RETURN)
        sleep(1)

        dept_yes = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/div/input[4]")
        dept_yes.send_keys(Keys.RETURN)
        sleep(1)
    
    def test_events(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)
        # -------------------------------------------EVENTS-----------------------------------------------------------------
        events = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/th/a')
        events.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # -------------------------------------------EVENTS_ADD-------------------------------------------------------------
        events_add = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/td[1]/a')
        events_add.send_keys(Keys.RETURN)
        sleep(1)

        events_name =self.driver.find_element_by_name('event_name')
        events_name.send_keys('python')
        sleep(1)

        events_date = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset[1]/div[2]/div/p/span[1]/a[1]')
        events_date.send_keys(Keys.RETURN)
        sleep(1)

        events_time = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset[1]/div[2]/div/p/span[2]/a[1]')
        events_time.send_keys(Keys.RETURN)
        sleep(1)

        events_enddate = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset[1]/div[3]/div/p/span[1]/a[1]')
        events_enddate.send_keys(Keys.RETURN)
        sleep(1)

        events_endtime  = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset[1]/div[3]/div/p/span[2]/a[1]')
        events_endtime.send_keys(Keys.RETURN)
        sleep(1)

        events_guest = self.driver.find_element_by_name("guest_fk")
        events_guest.send_keys("test_guest")

        events_max = self.driver.find_element_by_name('max_seats')
        events_max.send_keys('20')
        sleep(1)
        
        events_allow = self.driver.find_element_by_name("allow_ext")
        events_allow.click()
        sleep(1)
        events_dis = self.driver.find_element_by_name("description")
        events_dis.send_keys('python programming')
        sleep(1)
        events_sum = self.driver.find_element_by_name("summary")
        events_sum.send_keys("basic python programming")

        event_place = self.driver.find_element_by_name('place')
        event_place.send_keys('CIR BLOCK')
        sleep(1)

        events_savee = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]')
        events_savee.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # -------------------------------------------EVENTS_CHANGE---------------------------------------------------------
        event_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/td[2]/a"
        )
        event_change.send_keys(Keys.RETURN)
        sleep(1)

        event_b = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[1]")
        event_b.send_keys("python")
        sleep(1)

        event_se = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[2]")
        event_se.send_keys(Keys.RETURN)

        event_box = self.driver.find_element_by_name("_selected_action")
        event_box.click()
        
        event_action = self.driver.find_element_by_name("action")
        event_action.send_keys("Delete selected departments")

        event_go = self.driver.find_element_by_name("index")
        event_go.send_keys(Keys.RETURN)
        sleep(1)

        event_no = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        event_no.send_keys(Keys.RETURN)
        sleep(1)

        event_go = self.driver.find_element_by_name("index")
        event_go.send_keys(Keys.RETURN)
        sleep(1)

        event_yes = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/div/input[4]")
        event_yes.send_keys(Keys.RETURN)
        sleep(1)
    
    def test_externalusers(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)
        # ------------------------------------------EXTERNALUSERS----------------------------------------------------------
        externalusers = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/th/a"
        )
        externalusers.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # -----------------------------------------EXTERNALUSERS_ADD-----------------------------------------------------
        sleep(1)
        externalusers_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/td[1]/a"
        )
        externalusers_add.send_keys(Keys.RETURN)
        sleep(1)

        external_account = self.driver.find_element_by_name("account")
        external_account.send_keys("ext_stud")
        sleep(1)

        external_save = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]")
        external_save.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # ------------------------------------------EXTERNALUSER_CHANGE-----------------------------------------------------
        sleep(1)
        externaluser_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/td[2]/a"
        )
        externaluser_change.send_keys(Keys.RETURN)
        sleep(1)

        external_b = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[1]")
        external_b.send_keys("ext_stud")
        sleep(1)

        external_se = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[2]")
        external_se.send_keys(Keys.RETURN)

        external_box = self.driver.find_element_by_name("_selected_action")
        external_box.click()
        
        external_action = self.driver.find_element_by_name("action")
        external_action.send_keys("Delete selected departments")

        external_go = self.driver.find_element_by_name("index")
        external_go.send_keys(Keys.RETURN)
        sleep(1)

        external_no = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        external_no.send_keys(Keys.RETURN)
        sleep(1)

        external_go = self.driver.find_element_by_name("index")
        external_go.send_keys(Keys.RETURN)
        sleep(1)

        external_yes = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/div/input[4]")
        external_yes.send_keys(Keys.RETURN)
        sleep(1)

    def test_faculty(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)
        # -------------------------------------------FACULTY-------------------------------------------------------------
        faculty = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/th/a"
        )
        faculty.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # --------------------------------------------FACULTY_ADD-----------------------------------------------------
        faculty_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/td[1]/a"
        )
        faculty_add.send_keys(Keys.RETURN)
        sleep(1)

        faculty_account = self.driver.find_element_by_name("account")
        faculty_account.send_keys("test_fac")

        faculty_dep = self.driver.find_element_by_name("dept_fk")
        faculty_dep.send_keys("CSE")

        faculty_save = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]")
        faculty_save.send_keys(Keys.RETURN)

        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # -------------------------------------------FACULTY_CHANGE----------------------------------------------------
        faculty_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/td[2]/a"
        )
        faculty_change.send_keys(Keys.RETURN)
        sleep(1)

        faculty_b = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[1]")
        faculty_b.send_keys("test_fac")
        sleep(1)

        faculty_se = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[2]")
        faculty_se.send_keys(Keys.RETURN)

        faculty_box = self.driver.find_element_by_name("_selected_action")
        faculty_box.click()
        
        faculty_action = self.driver.find_element_by_name("action")
        faculty_action.send_keys("Delete selected departments")

        faculty_go = self.driver.find_element_by_name("index")
        faculty_go.send_keys(Keys.RETURN)
        sleep(1)

        faculty_no = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        faculty_no.send_keys(Keys.RETURN)
        sleep(1)

        faculty_go = self.driver.find_element_by_name("index")
        faculty_go.send_keys(Keys.RETURN)
        sleep(1)

        faculty_yes = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/div/input[4]")
        faculty_yes.send_keys(Keys.RETURN)
        sleep(1)

    
    def test_guests(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)
        # -------------------------------------------GUESTS-----------------------------------------------------------------
        guests = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[7]/th/a"
        )
        guests.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # -------------------------------------------GUESTS_ADD--------------------------------------------------------------
        guests_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[7]/td[1]/a"
        )
        guests_add.send_keys(Keys.RETURN)

        guest_acc = self.driver.find_element_by_name("account")
        guest_de = self.driver.find_element_by_name("details")
        guest_save = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]"
        )
        sleep(1)
        guest_acc.send_keys("test_guest1")
        guest_de.send_keys("From Banglore")
        guest_save.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # ------------------------------------------GUESTS_CHANGE-----------------------------------------------------------
        guests_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[7]/td[2]/a"
        )
        guests_change.send_keys(Keys.RETURN)
        sleep(1)

        guests_b = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[1]")
        guests_b.send_keys("test_guest1")
        sleep(1)

        guests_se = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[2]")
        guests_se.send_keys(Keys.RETURN)

        guests_box = self.driver.find_element_by_name("_selected_action")
        guests_box.click()
        
        guests_action = self.driver.find_element_by_name("action")
        guests_action.send_keys("Delete selected departments")

        guests_go = self.driver.find_element_by_name("index")
        guests_go.send_keys(Keys.RETURN)
        sleep(1)

        guests_no = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        guests_no.send_keys(Keys.RETURN)
        sleep(1)

        guests_go = self.driver.find_element_by_name("index")
        guests_go.send_keys(Keys.RETURN)
        sleep(1)

        guests_yes = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/div/input[4]")
        guests_yes.send_keys(Keys.RETURN)
        sleep(1)

    
    def test_students(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)
        # ------------------------------------------STUDENTS---------------------------------------------------------------
        students = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/th/a"
        )
        students.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # ---------------------------------------------STUDENTS_ADD-------------------------------------------------------
        students_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/td[1]/a"
        )
        students_add.send_keys(Keys.RETURN)
        sleep(1)
        stu_acc = self.driver.find_element_by_name("account")
        stu_regno = self.driver.find_element_by_name("reg_no")
        stu_dep = self.driver.find_element_by_name("dept_fk")
        stu_save = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]"
        )
        sleep(1)
        stu_acc.send_keys("test_stud")
        stu_regno.send_keys("18035")
        stu_dep.send_keys("Computer Science Engineering")
        stu_save.send_keys(Keys.RETURN)
        sleep(1)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get(self.live_server_url + "/admin/")
        # -------------------------------------------STUDENTS_CHANGE----------------------------------------------------
        student_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/td[2]/a"
        )
        student_change.send_keys(Keys.RETURN)
        sleep(1)
        student_b = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[1]")
        student_b.send_keys("test_stud")
        sleep(1)

        student_se = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[2]")
        student_se.send_keys(Keys.RETURN)

        student_box = self.driver.find_element_by_name("_selected_action")
        student_box.click()
        
        student_action = self.driver.find_element_by_name("action")
        student_action.send_keys("Delete selected departments")

        student_go = self.driver.find_element_by_name("index")
        student_go.send_keys(Keys.RETURN)
        sleep(1)

        student_no = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        student_no.send_keys(Keys.RETURN)
        sleep(1)

        student_go = self.driver.find_element_by_name("index")
        student_go.send_keys(Keys.RETURN)
        sleep(1)

        student_yes = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/div/input[4]")
        student_yes.send_keys(Keys.RETURN)
        sleep(1)
 

    def test_change_password(self):
        self.driver.get(self.live_server_url + "/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("test_admin")
        password.send_keys("test_admin_password")
        submit.send_keys(Keys.RETURN)

        sleep(3)
        changepassword = self.driver.find_element_by_xpath(
            "/html/body/div/div[1]/div[2]/a[2]"
        )
        changepassword.send_keys(Keys.RETURN)

        sleep(1)
        # self.driver.get('http://127.0.0.1:8000/admin/password_change/')

        oldpassword = self.driver.find_element_by_name("old_password")
        newpassword = self.driver.find_element_by_name("new_password1")
        newpasswordconfirmation = self.driver.find_element_by_name("new_password2")
        changemypassword = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input"
        )

        sleep(1)
        oldpassword.send_keys("test_admin_password")
        newpassword.send_keys("test_admin_password")
        newpasswordconfirmation.send_keys("test_admin_password")
        changemypassword.send_keys(Keys.RETURN)
        sleep(1)