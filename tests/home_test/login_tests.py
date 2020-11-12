import time
from pages.home_page.login_page import LoginPage
import unittest
import utilities.custom_logger as cl
import logging
import pytest
from pages.home_page.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
TestStatus.__test__ = False


# @pytest.mark.run(order=2)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    # log = cl.customLogger(logging.DEBUG)
    # log = cl.customLogger(logging.DEBUG, file_name="automation_test_suite")

    @pytest.fixture(autouse=True)
    def class_level_setup(self):
        self.login_page_obj = LoginPage(self.driver)
        self.test_status = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=4)
    def test_for_valid_login(self):
        self.nav.navigateToHomePage()

        self.login_page_obj.login("test@email.com", "abcabc")

        login_result1 = self.login_page_obj.verify_title()
        self.test_status.mark(login_result1, "Title Verification")

        login_result2 = self.login_page_obj.check_login_successful()
        self.test_status.markFinal("(Test for Valid Login)", login_result2,
                                   "<<<< Checked whether Login is Successful >>>>")

        self.nav.navigateToAllCourses()
        time.sleep(2)

    @pytest.mark.run(order=3)
    def test_for_invalid_login(self):
        self.login_page_obj.login()

        login_result = self.login_page_obj.check_login_failed()
        self.test_status.markFinal("(Test for In-Valid Login)", login_result,
                                   "<<<< Checked whether Login is Un-Successful >>>>")

    @pytest.mark.run(order=5)
    def test_for_logout(self):
        self.login_page_obj.logout()

        logout_result = self.login_page_obj.verify_logout_successful()
        self.test_status.markFinal("(Test for Logout)", logout_result,
                                   "<<<< Checked whether Logout is Successful >>>>")
