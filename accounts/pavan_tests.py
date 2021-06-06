from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LoginFormTest(LiveServerTestCase):

    def test_main_login_logout(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')

        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        submit = driver.find_element_by_name('submit')

        username.send_keys('pavan')
        password.send_keys('student/.,')
        submit.send_keys(Keys.RETURN)

        time.sleep(3)
        main_logout = driver.find_element_by_xpath(
            '/html/body/nav/div/div/div[3]/a')
        main_logout.send_keys(Keys.RETURN)

        time.sleep(3)
        driver.get('http://127.0.0.1:8000/accounts/logout/')
        main_loginagain = driver.find_element_by_xpath(
            '/html/body/div/div/a/button')
        main_loginagain.send_keys(Keys.RETURN)

        time.sleep(3)

    def test_from_main_to_admin_page(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')

        time.sleep(3)
        admin = driver.find_element_by_xpath('/html/body/div/div/span/a')
        admin.send_keys(Keys.RETURN)
        time.sleep(3)

    def test_mainfirstpage(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')

        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        submit = driver.find_element_by_name('submit')

        username.send_keys('pavan')
        password.send_keys('student/.,')
        submit.send_keys(Keys.RETURN)

        time.sleep(3)

        appliedevents = driver.find_element_by_xpath(
            '/html/body/div/div/div/div/div/div/ul/li[1]/p/a')
        appliedevents.send_keys(Keys.RETURN)

        time.sleep(3)
        driver.get('http://127.0.0.1:8000/applied_events/2/')
        linktoeventpage = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/a')
        linktoeventpage.send_keys(Keys.RETURN)

        # time.sleep(3)
        # driver.get('http://127.0.0.1:8000/2/event/1/')
        # eventsystem = driver.find_element_by_xpath('/html/body/nav/div/a/span')
        # eventsystem.send_keys(Keys.RETURN)

        time.sleep(3)
        driver.get('http://127.0.0.1:8000/')
        upcomingevents = driver.find_element_by_xpath(
            '/html/body/div/div/div/div/div/div/ul/li[2]/p/a')
        upcomingevents.send_keys(Keys.RETURN)

        time.sleep(3)
        driver.get('http://127.0.0.1:8000/')
        pastevents = driver.find_element_by_xpath(
            '/html/body/div/div/div/div/div/div/ul/li[3]/p/a')
        pastevents.send_keys(Keys.RETURN)

        time.sleep(3)
        assert 'pavan' in driver.page_source

    def test_admin_login_logout(self):
        driver = webdriver.Chrome()
        driver.get('http://localhost:8000/admin/')

        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        submit = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

        username.send_keys('admin')
        password.send_keys('student/.,')
        submit.send_keys(Keys.RETURN)

        time.sleep(3)
        admin_logout = driver.find_element_by_xpath(
            '/html/body/div/div[1]/div[2]/a[3]')
        admin_logout.send_keys(Keys.RETURN)

        time.sleep(3)
        # driver.get('http://127.0.0.1:8000/admin/logout/')
        admin_loginagain = driver.find_element_by_xpath(
            '/html/body/div/div[3]/div/div[1]/p[2]/a')
        admin_loginagain.send_keys(Keys.RETURN)

        time.sleep(3)

        assert 'admin' in driver.page_source

    # def test_adminfirstpage(self):
    #     driver = webdriver.Chrome()
    #     driver.get('http://localhost:8000/admin/')

    #     username = driver.find_element_by_name('username')
    #     password = driver.find_element_by_name('password')
    #     submit = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

    #     username.send_keys('admin')
    #     password.send_keys('student/.,')
    #     submit.send_keys(Keys.RETURN)
    #     # ---------------------------------------------USER------------------------------------------------------
    #     time.sleep(3)
    #     users = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr/th/a')
    #     users.send_keys(Keys.RETURN)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     time.sleep(3)
    #     driver.get('http://localhost:8000/admin/')
    #     # --------------------------------------------USER_ADD----------------------------------------------------
    #     time.sleep(2)
    #     user_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr/td[1]/a')
    #     user_add.send_keys(Keys.RETURN)

    #     username = driver.find_element_by_name('username')
    #     password = driver.find_element_by_name('password1')
    #     password_conformation = driver.find_element_by_name('password2')
    #     user_type = driver.find_element_by_name('user_type')
    #     phonenumber = driver.find_element_by_name('phone_no')
    #     save = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]')

    #     time.sleep(3)
    #     username.send_keys('s3')
    #     password.send_keys('student@#$3')
    #     password_conformation.send_keys('student@#$3')
    #     user_type.send_keys('student')
    #     phonenumber.send_keys('6302456778')
    #     save.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     first_name = driver.find_element_by_name('first_name')
    #     last_name = driver.find_element_by_name('last_name')
    #     email_address = driver.find_element_by_name('email')
    #     save = driver.find_element_by_xpath(
    #         '/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]')

    #     time.sleep(3)
    #     first_name.send_keys('student')
    #     last_name.send_keys('3')
    #     email_address.send_keys('student3@gmail.com')
    #     save.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------USER_CHANGE---------------------------------------------------------------
    #     user_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr/td[2]/a')
    #     user_change.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     block = driver.find_element_by_name('q')
    #     search = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/form/div/input[2]')

    #     time.sleep(3)
    #     block.send_keys('w')
    #     search.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     ac = driver.find_element_by_name('_selected_action')
    #     ac.click()

    #     time.sleep(3)
    #     action = driver.find_element_by_name('action')
    #     action.send_keys('Delete selected users')
    #     go = driver.find_element_by_name('index')
    #     go.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     takemeback = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/form/div/a')
    #     takemeback.send_keys(Keys.RETURN)
    #     go = driver.find_element_by_name('index')
    #     go.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     yes = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/form/div/input[4]')
    #     yes.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ---------------------------------------------GROUPS------------------------------------------------------------------
    #     groups = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/th/a')
    #     groups.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # --------------------------------------------GROUP_ADD------------------------------------------------------
    #     group_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/td[1]/a')
    #     group_add.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     grp_name = driver.find_element_by_name('name')
    #     chooseall = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/div[1]/div/div[1]/a')
    #     grp_save = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]')

    #     time.sleep(3)
    #     grp_name.send_keys('BBA')
    #     chooseall.click()
    #     grp_save.send_keys(Keys.RETURN)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ------------------------------------------GROUP_CHANGE------------------------------------------------------------
    #     group_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/td[2]/a')
    #     group_change.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     grp_name = driver.find_element_by_name('q')
    #     grp_x = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/form/div/input[2]')

    #     time.sleep(3)
    #     grp_name.send_keys('EEE')
    #     grp_x.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     grp_sa = driver.find_element_by_name('_selected_action')
    #     grp_sa.click()

    #     time.sleep(3)
    #     grp_action = driver.find_element_by_name('action')
    #     grp_action.send_keys('Delete selected users')
    #     grp_go = driver.find_element_by_name('index')
    #     grp_go.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     grp_takemeback = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/form/div/a')
    #     grp_takemeback.send_keys(Keys.RETURN)
    #     grp_go = driver.find_element_by_name('index')
    #     grp_go.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     grp_yes = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/form/div/input[4]')
    #     grp_yes.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------APPLICATIONS------------------------------------------------------------
    #     applications = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/th/a')
    #     applications.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # driver.get('http://localhost:8000/admin/')
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # --------------------------------------------APPLICATION_ADD--------------------------------------------------------
    #     application_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/a')
    #     application_add.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ---------------------------------------------APPLICATION_CHANGE--------------------------------------------------
    #     application_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]/a')
    #     application_change.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------CIR FACULTY------------------------------------------------------------
    #     cirfaculty = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/th/a')
    #     cirfaculty.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # --------------------------------------------CIR FACULTY_ADD---------------------------------------------------------
    #     cirfaculty_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[1]/a')
    #     cirfaculty_add.send_keys(Keys.RETURN)

    #     pluscir = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div/div/div/a[2]/img')
    #     pluscir.click()

    #     usercir = driver.find_element_by_name('username')
    #     passcir = driver.find_element_by_name('password1')
    #     passconcir = driver.find_element_by_name('password2')
    #     typecir = driver.find_element_by_name('user_type')
    #     phonecir = driver.find_element_by_name('phone_no')
    #     savecir = driver.find_element_by_xpath(
    #         '/html/body/div/div/div/div[1]/div/form/div/div/input')

    #     time.sleep(3)
    #     usercir.send_keys('cir3')
    #     passcir.send_keys('cir3!@#123')
    #     passconcir.send_keys('cir3!@#123')
    #     typecir.send_keys('CIR Faculty')
    #     phonecir.send_keys('6302341234')
    #     savecir.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     cirfaculty_se = driver.find_element_by_name('account')
    #     cirfaculty_se.send_keys('cir3')

    #     cirfaculty_c = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div/div/div/a[1]/img')
    #     cirfaculty_c.click()

    #     time.sleep(3)
    #     cirfaculty_first_name = driver.find_element_by_name('first_name')
    #     cirfaculty_last_name = driver.find_element_by_name('last_name')
    #     cirfaculty_email_address = driver.find_element_by_name('email')
    #     cirfaculty_staff = driver.find_element_by_name('is_staff')
    #     cirfaculty_selectall = driver.find_element_by_xpath(
    #         '/html/body/div[1]/div/div/div[1]/div/form/div/fieldset[3]/div[4]/div/div[1]/div/div[1]/a')
    #     cirfaculty_chooseall = driver.find_element_by_xpath(
    #         '/html/body/div[1]/div/div/div[1]/div/form/div/fieldset[3]/div[5]/div/div[1]/div/div[1]/a')
    #     cirfaculty_sav = driver.find_element_by_xpath(
    #         '/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]')

    #     time.sleep(3)
    #     cirfaculty_first_name.send_keys('cir')
    #     cirfaculty_last_name.send_keys('faculty2')
    #     cirfaculty_email_address.send_keys('cirfaculty2@gmail.com')
    #     cirfaculty_staff.click()
    #     cirfaculty_selectall.click()
    #     cirfaculty_chooseall.click()
    #     cirfaculty_sav.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ------------------------------------------CIR FACULTY_CHANGE---------------------------------------------------------
    #     cirfaculty_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/a')
    #     cirfaculty_change.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ------------------------------------------DEPARTMENTS------------------------------------------------------------
    #     departments = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/th/a')
    #     departments.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ------------------------------------------DEPARTMENTS_ADD---------------------------------------------------------
    #     departments_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[1]/a')
    #     departments_add.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     dept_code = driver.find_element_by_name('dept_code')
    #     dept_name = driver.find_element_by_name('dept_name')
    #     dept_save = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]')

    #     time.sleep(3)
    #     dept_code.send_keys('CE')
    #     dept_name.send_keys('Civil Engineering')
    #     dept_save.send_keys(Keys.RETURN)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------DEPARTMENT_CHANGE-----------------------------------------------
    #     department_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[2]/a')
    #     department_change.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     dept_box = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/div/div/form/div[2]/table/thead/tr/th[1]/div[1]/span/input')
    #     dept_action = driver.find_element_by_name('action')
    #     dept_go = driver.find_element_by_name('index')
    #     # dept_selected = driver.find_element_by_xpath('_selected_action')
    #     # dept_selected.click()
    #     time.sleep(3)
    #     dept_box.click()
    #     dept_action.send_keys('Delete selected departments')
    #     time.sleep(3)
    #     dept_go.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     dept_no = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/form/div/a')
    #     dept_no.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     dept_go = driver.find_element_by_name('index')
    #     dept_go.send_keys(Keys.RETURN)
    #     time.sleep(3)

    #     dept_yes = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/form/div/input[7]')
    #     dept_yes.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------EVENTS-----------------------------------------------------------------
    #     events = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/th/a')
    #     events.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------EVENTS_ADD-------------------------------------------------------------
    #     events_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/td[1]/a')
    #     events_add.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------EVENTS_CHANGE---------------------------------------------------------
    #     event_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[4]/td[2]/a')
    #     event_change.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ------------------------------------------EXTERNALUSERS----------------------------------------------------------
    #     externalusers = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/th/a')
    #     externalusers.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -----------------------------------------EXTERNALUSERS_ADD-----------------------------------------------------
    #     externalusers_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/td[1]/a')
    #     externalusers_add.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ------------------------------------------EXTERNALUSER_CHANGE-----------------------------------------------------
    #     externaluser_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[5]/td[2]/a')
    #     externaluser_change.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------FACULTY-------------------------------------------------------------
    #     faculty = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/th/a')
    #     faculty.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # --------------------------------------------FACULTY_ADD-----------------------------------------------------
    #     faculty_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/td[1]/a')
    #     faculty_add.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------FACULTY_CHANGE----------------------------------------------------
    #     faculty_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[6]/td[2]/a')
    #     faculty_change.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------GUESTS-----------------------------------------------------------------
    #     guests = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[7]/th/a')
    #     guests.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------GUESTS_ADD--------------------------------------------------------------
    #     guests_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[7]/td[1]/a')
    #     guests_add.send_keys(Keys.RETURN)

    #     guest_acc = driver.find_element_by_name('account')
    #     guest_de = driver.find_element_by_name('details')
    #     guest_save = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]')
    #     time.sleep(3)
    #     guest_acc.send_keys('guest1')
    #     guest_de.send_keys('From Banglore')
    #     guest_save.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ------------------------------------------GUESTS_CHANGE-----------------------------------------------------------
    #     guests_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[7]/td[2]/a')
    #     guests_change.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ------------------------------------------STUDENTS---------------------------------------------------------------
    #     students = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/th/a')
    #     students.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # ---------------------------------------------STUDENTS_ADD-------------------------------------------------------
    #     students_add = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/td[1]/a')
    #     students_add.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     stu_acc = driver.find_element_by_name('account')
    #     stu_regno = driver.find_element_by_name('reg_no')
    #     stu_dep = driver.find_element_by_name('dept_fk')
    #     stu_save = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]')
    #     time.sleep(3)
    #     stu_acc.send_keys('s2')
    #     stu_regno.send_keys('18002')
    #     stu_dep.send_keys('Computer Science Engineering')
    #     stu_save.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     # -----------------------------------------RETURN TO HOME PAGE-----------------------------------------------
    #     driver.get('http://localhost:8000/admin/')
    #     # -------------------------------------------STUDENTS_CHANGE----------------------------------------------------
    #     student_change = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr[8]/td[2]/a')
    #     student_change.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     assert 'admin' in driver.page_source

    # def test_change_password(self):
    #     driver = webdriver.Chrome()
    #     driver.get('http://localhost:8000/admin/')

    #     username = driver.find_element_by_name('username')
    #     password = driver.find_element_by_name('password')
    #     submit = driver.find_element_by_xpath(
    #         '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')

    #     username.send_keys('admin')
    #     password.send_keys('student/.,')
    #     submit.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     changepassword = driver.find_element_by_xpath(
    #         '/html/body/div/div[1]/div[2]/a[2]')
    #     changepassword.send_keys(Keys.RETURN)

    #     time.sleep(3)
    #     # driver.get('http://127.0.0.1:8000/admin/password_change/')

    #     oldpassword = driver.find_element_by_name('old_password')
    #     newpassword = driver.find_element_by_name('new_password1')
    #     newpasswordconfirmation = driver.find_element_by_name('new_password2')
    #     changemypassword = driver.find_element_by_xpath(
    #         '/html/body/div/div[3]/div/div[1]/div/form/div/div/input')

    #     time.sleep(3)
    #     oldpassword.send_keys('student/.,')
    #     newpassword.send_keys('student/.,')
    #     newpasswordconfirmation.send_keys('student/.,')
    #     changemypassword.send_keys(Keys.RETURN)

    #     time.sleep(3)
