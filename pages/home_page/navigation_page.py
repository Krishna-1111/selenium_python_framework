import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):

    # log = cl.customLogger(logging.DEBUG)
    # log = cl.customLogger(logging.DEBUG, file_name="automation_exercise_ddt_csv")
    log = cl.customLogger(logging.DEBUG, file_name="automation_test_suite")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses_loc_value = "My Courses"
    _all_courses_loc_value = "All Courses"
    _practice_loc_value = "Practice"
    _user_settings_icon_loc_value = "//div[@id='navbar']//li[@class='dropdown']"
    _lets_kode_it_icon_loc_value = "//a[@class='navbar-brand header-logo']"
    # Locator Types
    _my_courses_loc_type = "link"
    _all_courses_loc_type = "link"
    _practice_loc_type = "link"
    _user_settings_icon_loc_type = "xpath"
    _lets_kode_it_icon_loc_type = "xpath"

    def navigateToHomePage(self):
        self.elementClick(locator=self._lets_kode_it_icon_loc_value, locatorType=self._lets_kode_it_icon_loc_type)

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses_loc_value, locatorType=self._all_courses_loc_type)

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses_loc_value, locatorType=self._my_courses_loc_type)

    def navigateToPractice(self):
        self.elementClick(locator=self._practice_loc_value, locatorType=self._practice_loc_type)

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon_loc_value,
                                                  locatorType=self._user_settings_icon_loc_type, pollFrequency=1)
        self.elementClick(element=userSettingsElement)
        # self.elementClick(locator=self._user_settings_icon, locatorType="xpath")
