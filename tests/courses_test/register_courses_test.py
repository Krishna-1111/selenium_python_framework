import unittest
import pytest
from pages.cources_page.register_courses_page import RegisterCoursePage
from utilities.teststatus import TestStatus
TestStatus.__test__ = False


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTests(unittest.TestCase):

    @pytest.yield_fixture(autouse=True)
    def class_level_setup(self):
        self.course_page_obj = RegisterCoursePage(self.driver)
        self.test_status_obj = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_for_login(self):
        self.course_page_obj.login("test11@email.com", "letsautomate")
        result = self.course_page_obj.verify_login_successful()
        self.test_status_obj.markFinal("(test_for_login)", result, "Login Verification")

    @pytest.mark.run(order=2)
    def test_for_course_registration(self):
        self.course_page_obj.register_course()
        result = self.course_page_obj._register_val_results
        if False not in result:
            self.test_status_obj.markFinal("(test_for_course_registration)", result=True,
                                           resultMessage="Course Registration Verification")
        else:
            self.test_status_obj.markFinal("(test_for_course_registration)", result=False,
                                           resultMessage="Course Registration Verification")










