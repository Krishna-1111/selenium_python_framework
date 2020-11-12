import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home_page.navigation_page import NavigationPage


class LoginPage(BasePage):

    # log = cl.customLogger(logging.DEBUG)
    log = cl.customLogger(logging.DEBUG, file_name="automation_test_suite")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link_loc_value = "Login"
    _email_field_loc_value = "user_email"
    _password_field_loc_value = "user_password"
    _login_button_loc_value = "commit"
    _invalid_credentials_msg_loc_value = "//div[contains(text(),'Invalid email or password')]"
    _user_icon_loc_value = "//div[@id='navbar']//img[@class='gravatar']"
    _logout_loc_value = "//a[contains(text(),'Log Out')]"
    _home_page_loc_value = "//div[@id='blocks']//div[@class='homepage-hero']"
    # Locator types
    _login_link_loc_type = "link"
    _email_field_loc_type = "id"
    _password_field_loc_type = "id"
    _login_button_loc_type = "name"
    _invalid_credentials_msg_loc_type = "xpath"
    _user_icon_loc_type = "xpath"
    _logout_loc_type = "xpath"
    _home_page_loc_type = "xpath"

    def _click_login_link(self):
        self.elementClick(self._login_link_loc_value, locatorType=self._login_link_loc_type)

    def _enter_email(self, email):
        self.sendKeys(email, self._email_field_loc_value, locatorType=self._email_field_loc_type)

    def _enter_password(self, password):
        self.sendKeys(password, self._password_field_loc_value, locatorType=self._password_field_loc_type)

    def _click_login_button(self):
        self.elementClick(self._login_button_loc_value, locatorType=self._login_button_loc_type)

    def _clear_fields(self):
        email_field = self.getElement(locator=self._email_field_loc_value)
        email_field.clear()
        password_field = self.getElement(locator=self._password_field_loc_value)
        password_field.clear()

    def login(self, email="", password=""):
        self._click_login_link()
        time.sleep(2)
        self._enter_email(email)
        self._enter_password(password)
        self._click_login_button()

    def check_login_successful(self):
        login_successful_element = self.waitForElement(locator=self._user_icon_loc_value,
                                                       locatorType=self._user_icon_loc_type, timeout=5)
        result = self.isElementPresent(element=login_successful_element)
        return result

    def check_login_failed(self):
        login_failed_element = self.waitForElement(locator=self._invalid_credentials_msg_loc_value,
                                                   locatorType=self._invalid_credentials_msg_loc_type, timeout=30)
        result = self.isElementPresent(element=login_failed_element)
        return result

    def verify_title(self):
        return self.verifyPageTitle("let's kode it")

    def logout(self):
        self.nav.navigateToUserSettings()
        logout_element = self.waitForElement(locator=self._logout_loc_value, locatorType=self._logout_loc_type,
                                             timeout=10)
        self.elementClick(element=logout_element)

    def verify_logout_successful(self):
        home_page_element = self.waitForElement(locator=self._home_page_loc_value,
                                                locatorType=self._home_page_loc_type, timeout=30)
        result = self.isElementPresent(element=home_page_element)
        return result

    # ----------------------------------Deprecated page class methods-----------------------------------------
    # def _get_login_link(self):
    #     return self.driver.find_element(self._login_link_loc_type, self._login_link_loc_value)
    #
    # def _get_email_field(self):
    #     return self.driver.find_element(self._email_field_loc_type, self._email_field_loc_value)
    #
    # def _get_password_field(self):
    #     return self.driver.find_element(self._password_field_loc_type, self._password_field_loc_value)
    #
    # def _get_login_button(self):
    #     return self.driver.find_element(self._login_button_loc_type, self._login_button_loc_value)
    #
    # def _click_login_link(self):
    #     self._get_login_link().click()
    #
    # def _enter_email(self, email):
    #     self._get_email_field().send_keys(email)
    #
    # def _enter_password(self, password):
    #     self._get_password_field().send_keys(password)
    #
    # def _click_login_button(self):
    #     self._get_login_button().click()
    # ------------------------------------------------------------------------------------------------------------

    # ----------------------------------------Initial page class method------------------------------------------------
    # def login(self, username, password):
    #     time.sleep(3)
    #     login_link = self.driver.find_element(By.LINK_TEXT, "Login")
    #     login_link.click()
    #
    #     time.sleep(2)
    #     email_field = self.driver.find_element(By.ID, "user_email")
    #     email_field.send_keys(username)
    #
    #     time.sleep(3)
    #     password_field = self.driver.find_element(By.ID, "user_password")
    #     password_field.send_keys(password)
    #     time.sleep(3)
    #
    #     time.sleep(3)
    #     login_button = self.driver.find_element(By.NAME, "commit")
    #     login_button.click()
    #     time.sleep(30)
    # -------------------------------------------------------------------------------------------------------------
