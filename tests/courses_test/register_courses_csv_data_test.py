from pages.cources_page.register_courses_page import RegisterCoursePage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home_page.navigation_page import NavigationPage
TestStatus.__test__ = False


# @pytest.mark.run(order=1)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_level_setup(self):
        self.course_page_obj = RegisterCoursePage(self.driver)
        self.test_status_obj = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.fixture(autouse=False)
    def setter(self):
        self.nav.navigateToHomePage()

    @pytest.mark.run(order=1)
    @data(*getCSVData("F:\\Pycharm_Projects\\Automation_Framework\\testdata_t1.csv"))
    @unpack
    def test_for_login(self, t1_email, t1_password, t1_name, t1_info):
        self.course_page_obj.login(t1_email, t1_password)
        result = self.course_page_obj.verify_login_successful()
        if result is False:
            self.course_page_obj.clearField(locator=self.course_page_obj._email_field_loc_value,
                                            locatorType=self.course_page_obj._email_field_loc_type)
            self.course_page_obj.clearField(locator=self.course_page_obj._password_field_loc_value,
                                            locatorType=self.course_page_obj._password_field_loc_type)
        self.test_status_obj.markFinal(t1_name, result, t1_info)

    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures("setter")
    @data(*getCSVData("F:\\Pycharm_Projects\\Automation_Framework\\testdata_t2.csv"))
    @unpack
    def test_for_course_registration(self, t2_course_name, t2_keywrd, t2_cc_num, t2_exp_date, t2_cvc_num, t2_name,
                                     t2_info):
        self.course_page_obj.register_course(t2_course_name, t2_keywrd, t2_cc_num, t2_exp_date, t2_cvc_num)
        result = self.course_page_obj._register_val_results
        if False not in result:
            self.test_status_obj.markFinal(t2_name, result=True,
                                           resultMessage=t2_info)
        else:
            self.test_status_obj.markFinal(t2_name, result=False,
                                           resultMessage=t2_info)