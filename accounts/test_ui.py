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

    def test_login_form(self):
        self.driver.get(self.live_server_url)
        self.driver.implicitly_wait(15)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_name('submit')

        username.send_keys('test_username')
        password.send_keys('test_password')
        submit.send_keys(Keys.RETURN)

        assert 'test_username' in self.driver.page_source

    def test_admin_page_login(self):
        self.driver.get(self.live_server_url)
        self.driver.implicitly_wait(15)

        self.driver.find_element_by_link_text('admin').click()
        sleep(1)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

        username.send_keys('test_admin')
        password.send_keys('test_admin_password')
        submit.send_keys(Keys.RETURN)

        sleep(1)
        # ele = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.link_text, "Courses"))
        # )
        assert 'test_admin' in self.driver.page_source


class AdminSiteTest(LiveServerTestCase):
    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_adminfirstpage(self):
        self.driver.get("http://localhost:8000/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("admin")
        password.send_keys("student/.,")
        submit.send_keys(Keys.RETURN)
        # ---------------------------------------------USER------------------------------------------------------
        sleep(3)
        users = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr/th/a"
        )
        users.send_keys(Keys.RETURN)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        sleep(3)
        self.driver.get("http://localhost:8000/admin/")
        # --------------------------------------------USER_ADD----------------------------------------------------
        sleep(2)
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

        sleep(3)
        username.send_keys("s3")
        password.send_keys("student@#$3")
        password_conformation.send_keys("student@#$3")
        user_type.send_keys("student")
        phonenumber.send_keys("6302456778")
        save.send_keys(Keys.RETURN)
        sleep(3)

        first_name = self.driver.find_element_by_name("first_name")
        last_name = self.driver.find_element_by_name("last_name")
        email_address = self.driver.find_element_by_name("email")
        save = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]"
        )

        sleep(3)
        first_name.send_keys("student")
        last_name.send_keys("3")
        email_address.send_keys("student3@gmail.com")
        save.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------USER_CHANGE---------------------------------------------------------------
        user_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr/td[2]/a"
        )
        user_change.send_keys(Keys.RETURN)
        sleep(3)

        block = self.driver.find_element_by_name("q")
        search = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/form/div/input[2]"
        )

        sleep(3)
        block.send_keys("w")
        search.send_keys(Keys.RETURN)

        sleep(3)
        ac = self.driver.find_element_by_name("_selected_action")
        ac.click()

        sleep(3)
        action = self.driver.find_element_by_name("action")
        action.send_keys("Delete selected users")
        go = self.driver.find_element_by_name("index")
        go.send_keys(Keys.RETURN)

        sleep(3)
        takemeback = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        takemeback.send_keys(Keys.RETURN)
        go = self.driver.find_element_by_name("index")
        go.send_keys(Keys.RETURN)

        sleep(3)
        yes = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/input[4]"
        )
        yes.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ---------------------------------------------GROUPS------------------------------------------------------------------
        groups = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/th/a"
        )
        groups.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # --------------------------------------------GROUP_ADD------------------------------------------------------
        group_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/td[1]/a"
        )
        group_add.send_keys(Keys.RETURN)
        sleep(3)

        grp_name = self.driver.find_element_by_name("name")
        chooseall = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/div[1]/div/div[1]/a"
        )
        grp_save = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]"
        )

        sleep(3)
        grp_name.send_keys("BBA")
        chooseall.click()
        grp_save.send_keys(Keys.RETURN)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ------------------------------------------GROUP_CHANGE------------------------------------------------------------
        group_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/td[2]/a"
        )
        group_change.send_keys(Keys.RETURN)
        sleep(3)

        grp_name = self.driver.find_element_by_name("q")
        grp_x = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/form/div/input[2]"
        )

        sleep(3)
        grp_name.send_keys("EEE")
        grp_x.send_keys(Keys.RETURN)

        sleep(3)
        grp_sa = self.driver.find_element_by_name("_selected_action")
        grp_sa.click()

        sleep(3)
        grp_action = self.driver.find_element_by_name("action")
        grp_action.send_keys("Delete selected users")
        grp_go = self.driver.find_element_by_name("index")
        grp_go.send_keys(Keys.RETURN)

        sleep(3)
        grp_takemeback = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        grp_takemeback.send_keys(Keys.RETURN)
        grp_go = self.driver.find_element_by_name("index")
        grp_go.send_keys(Keys.RETURN)

        sleep(3)
        grp_yes = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/input[4]"
        )
        grp_yes.send_keys(Keys.RETURN)
        sleep(3)

        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------APPLICATIONS------------------------------------------------------------
        applications = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/th/a"
        )
        applications.send_keys(Keys.RETURN)
        sleep(3)
        # self.driver.get('http://localhost:8000/admin/')
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # --------------------------------------------APPLICATION_ADD--------------------------------------------------------
        application_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/a"
        )
        application_add.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ---------------------------------------------APPLICATION_CHANGE--------------------------------------------------
        application_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]/a"
        )
        application_change.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------CIR FACULTY------------------------------------------------------------
        cirfaculty = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/th/a"
        )
        cirfaculty.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # --------------------------------------------CIR FACULTY_ADD---------------------------------------------------------
        cirfaculty_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[1]/a"
        )
        cirfaculty_add.send_keys(Keys.RETURN)

        pluscir = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div/div/div/a[2]/img"
        )
        pluscir.click()

        usercir = self.driver.find_element_by_name("username")
        passcir = self.driver.find_element_by_name("password1")
        passconcir = self.driver.find_element_by_name("password2")
        typecir = self.driver.find_element_by_name("user_type")
        phonecir = self.driver.find_element_by_name("phone_no")
        savecir = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div/form/div/div/input"
        )

        sleep(3)
        usercir.send_keys("cir3")
        passcir.send_keys("cir3!@#123")
        passconcir.send_keys("cir3!@#123")
        typecir.send_keys("CIR Faculty")
        phonecir.send_keys("6302341234")
        savecir.send_keys(Keys.RETURN)

        sleep(3)
        cirfaculty_se = self.driver.find_element_by_name("account")
        cirfaculty_se.send_keys("cir3")

        cirfaculty_c = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div/div/div/a[1]/img"
        )
        cirfaculty_c.click()

        sleep(3)
        cirfaculty_first_name = self.driver.find_element_by_name("first_name")
        cirfaculty_last_name = self.driver.find_element_by_name("last_name")
        cirfaculty_email_address = self.driver.find_element_by_name("email")
        cirfaculty_staff = self.driver.find_element_by_name("is_staff")
        cirfaculty_selectall = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/form/div/fieldset[3]/div[4]/div/div[1]/div/div[1]/a"
        )
        cirfaculty_chooseall = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/form/div/fieldset[3]/div[5]/div/div[1]/div/div[1]/a"
        )
        cirfaculty_sav = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]"
        )

        sleep(3)
        cirfaculty_first_name.send_keys("cir")
        cirfaculty_last_name.send_keys("faculty2")
        cirfaculty_email_address.send_keys("cirfaculty2@gmail.com")
        cirfaculty_staff.click()
        cirfaculty_selectall.click()
        cirfaculty_chooseall.click()
        cirfaculty_sav.send_keys(Keys.RETURN)
        sleep(3)

        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ------------------------------------------CIR FACULTY_CHANGE---------------------------------------------------------
        cirfaculty_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/a"
        )
        cirfaculty_change.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ------------------------------------------DEPARTMENTS------------------------------------------------------------
        departments = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/th/a"
        )
        departments.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ------------------------------------------DEPARTMENTS_ADD---------------------------------------------------------
        departments_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[1]/a"
        )
        departments_add.send_keys(Keys.RETURN)
        sleep(3)

        dept_code = self.driver.find_element_by_name("dept_code")
        dept_name = self.driver.find_element_by_name("dept_name")
        dept_save = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]"
        )

        sleep(3)
        dept_code.send_keys("CE")
        dept_name.send_keys("Civil Engineering")
        dept_save.send_keys(Keys.RETURN)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------DEPARTMENT_CHANGE-----------------------------------------------
        department_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[2]/a"
        )
        department_change.send_keys(Keys.RETURN)

        sleep(3)
        dept_box = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/div/div/form/div[2]/table/thead/tr/th[1]/div[1]/span/input"
        )
        dept_action = self.driver.find_element_by_name("action")
        dept_go = self.driver.find_element_by_name("index")
        # dept_selected = self.driver.find_element_by_xpath('_selected_action')
        # dept_selected.click()
        sleep(3)
        dept_box.click()
        dept_action.send_keys("Delete selected departments")
        sleep(3)
        dept_go.send_keys(Keys.RETURN)
        sleep(3)

        dept_no = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/a"
        )
        dept_no.send_keys(Keys.RETURN)
        sleep(3)

        dept_go = self.driver.find_element_by_name("index")
        dept_go.send_keys(Keys.RETURN)
        sleep(3)

        dept_yes = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/input[7]"
        )
        dept_yes.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------EVENTS-----------------------------------------------------------------
        events = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/th/a"
        )
        events.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------EVENTS_ADD-------------------------------------------------------------
        events_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/td[1]/a"
        )
        events_add.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------EVENTS_CHANGE---------------------------------------------------------
        event_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/td[2]/a"
        )
        event_change.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ------------------------------------------EXTERNALUSERS----------------------------------------------------------
        externalusers = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/th/a"
        )
        externalusers.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -----------------------------------------EXTERNALUSERS_ADD-----------------------------------------------------
        externalusers_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/td[1]/a"
        )
        externalusers_add.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ------------------------------------------EXTERNALUSER_CHANGE-----------------------------------------------------
        externaluser_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/td[2]/a"
        )
        externaluser_change.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------FACULTY-------------------------------------------------------------
        faculty = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/th/a"
        )
        faculty.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # --------------------------------------------FACULTY_ADD-----------------------------------------------------
        faculty_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/td[1]/a"
        )
        faculty_add.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------FACULTY_CHANGE----------------------------------------------------
        faculty_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/td[2]/a"
        )
        faculty_change.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------GUESTS-----------------------------------------------------------------
        guests = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[7]/th/a"
        )
        guests.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
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
        sleep(3)
        guest_acc.send_keys("guest1")
        guest_de.send_keys("From Banglore")
        guest_save.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ------------------------------------------GUESTS_CHANGE-----------------------------------------------------------
        guests_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[7]/td[2]/a"
        )
        guests_change.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ------------------------------------------STUDENTS---------------------------------------------------------------
        students = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/th/a"
        )
        students.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # ---------------------------------------------STUDENTS_ADD-------------------------------------------------------
        students_add = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/td[1]/a"
        )
        students_add.send_keys(Keys.RETURN)
        sleep(3)
        stu_acc = self.driver.find_element_by_name("account")
        stu_regno = self.driver.find_element_by_name("reg_no")
        stu_dep = self.driver.find_element_by_name("dept_fk")
        stu_save = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]"
        )
        sleep(3)
        stu_acc.send_keys("s2")
        stu_regno.send_keys("18002")
        stu_dep.send_keys("Computer Science Engineering")
        stu_save.send_keys(Keys.RETURN)
        sleep(3)
        # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
        self.driver.get("http://localhost:8000/admin/")
        # -------------------------------------------STUDENTS_CHANGE----------------------------------------------------
        student_change = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/td[2]/a"
        )
        student_change.send_keys(Keys.RETURN)
        sleep(3)
        assert "admin" in self.driver.page_source

    def test_change_password(self):
        self.driver.get("http://localhost:8000/admin/")

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input"
        )

        username.send_keys("admin")
        password.send_keys("student/.,")
        submit.send_keys(Keys.RETURN)

        sleep(3)
        changepassword = self.driver.find_element_by_xpath(
            "/html/body/div/div[1]/div[2]/a[2]"
        )
        changepassword.send_keys(Keys.RETURN)

        sleep(3)
        # self.driver.get('http://127.0.0.1:8000/admin/password_change/')

        oldpassword = self.driver.find_element_by_name("old_password")
        newpassword = self.driver.find_element_by_name("new_password1")
        newpasswordconfirmation = self.driver.find_element_by_name("new_password2")
        changemypassword = self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/form/div/div/input"
        )

        sleep(3)
        oldpassword.send_keys("student/.,")
        newpassword.send_keys("student/.,")
        newpasswordconfirmation.send_keys("student/.,")
        changemypassword.send_keys(Keys.RETURN)

        sleep(3)
