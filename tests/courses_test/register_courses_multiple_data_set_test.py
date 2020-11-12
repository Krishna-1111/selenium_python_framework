from pages.cources_page.register_courses_page import RegisterCoursePage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
TestStatus.__test__ = False


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_level_setup(self):
        self.course_page_obj = RegisterCoursePage(self.driver)
        self.test_status_obj = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("test09@email.com", "letsautomate", "(test_for_login)", "Login Verification"),
          ("test10@email.com", "letsautomate", "(test_for_login)", "Login Verification"),
          ("test11@email.com", "letsautomate", "(test_for_login)", "Login Verification"))
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
    @data(("JavaScript", "beginners", "2341234569866550", "11/25", "112", "(test_for_course_registration)", "Course Registration Verification"),
          ("Selenium", "3.x", "2341234569866550", "09/25", "111", "(test_for_course_registration)", "Course Registration Verification"),
          ("Python", "from scratch", "2341234569866550", "08/22", "009", "(test_for_course_registration)", "Course Registration Verification"),
          ("Test", "NG", "2341234569866550", "11/27", "112", "(test_for_course_registration)", "Course Registration Verification"))
    @unpack
    def test_for_course_registration(self, t2_course_name, t2_keywrd, t2_cc_num, t2_exp_date, t2_cvc_num, t2_name, t2_info):
        self.course_page_obj.register_course(t2_course_name, t2_keywrd, t2_cc_num, t2_exp_date, t2_cvc_num)
        result = self.course_page_obj._register_val_results
        if False not in result:
            self.test_status_obj.markFinal(t2_name, result=True,
                                           resultMessage=t2_info)
        else:
            self.test_status_obj.markFinal(t2_name, result=False,
                                           resultMessage=t2_info)
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
        # self.driver.get("https://learn.letskodeit.com/courses")
