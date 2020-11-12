import time
from base.basepage import BasePage
from utilities.teststatus import TestStatus
import logging
import utilities.custom_logger as cl


class RegisterCoursePage(BasePage):

    # log = cl.customLogger(logging.DEBUG, file_name="automation_exercise")
    # log = cl.customLogger(logging.DEBUG, file_name="automation_exercise_ddt")
    # log = cl.customLogger(logging.DEBUG, file_name="automation_exercise_ddt_csv")
    log = cl.customLogger(logging.DEBUG, file_name="automation_test_suite")

    def __init__(self, driver):
        super(RegisterCoursePage, self).__init__(driver)
        self.driver = driver
        self.page_test_status_obj = TestStatus(driver)

    # Locators
    _login_link_loc_value = "Login"
    _email_field_loc_value = "user_email"
    _password_field_loc_value = "user_password"
    _login_button_loc_value = "commit"
    _user_icon_loc_value = "//div[@id='navbar']//img[@class='gravatar']"
    # Locator types
    _login_link_loc_type = "link"
    _email_field_loc_type = "id"
    _password_field_loc_type = "id"
    _login_button_loc_type = "name"
    _user_icon_loc_type = "xpath"

    def _click_login_link(self):
        self.elementClick(self._login_link_loc_value, locatorType=self._login_link_loc_type)

    def _enter_email(self, email):
        self.sendKeys(email, self._email_field_loc_value, locatorType=self._email_field_loc_type)

    def _enter_password(self, password):
        self.sendKeys(password, self._password_field_loc_value, locatorType=self._password_field_loc_type)

    def _click_login_button(self):
        self.elementClick(self._login_button_loc_value, locatorType=self._login_button_loc_type)

    def login(self, email="", password=""):
        self._click_login_link()
        time.sleep(2)
        self._enter_email(email)
        self._enter_password(password)
        self._click_login_button()

    def verify_login_successful(self):
        element = self.waitForElement(locator=self._user_icon_loc_value,
                                      locatorType=self._user_icon_loc_type, timeout=30)
        result = self.isElementPresent(element=element)
        return result

    # Default course registration details
    _course_search_name = "JavaScript"
    _keyword_of_interest = "beginner"
    _credit_card_no_val = 2341234569866550
    _credit_card_no_inval = 1234123412341234
    _valid_thru_date = "11/25"
    _cvv_no = 112
    _postal_code_no = 600018
    # Locators
    _search_course_text_loc_value = "search-courses"
    _search_icon_loc_value = "search-course-button"
    _courses_names_loc_value = "course-listing-title"
    _course_enroll_loc_value = "enroll-button-top"
    _iframe_cc_no_loc_value = "__privateStripeFrame5575"
    _iframe_exp_date_loc_value = "__privateStripeFrame5576"
    _iframe_cvc_no_loc_value = "__privateStripeFrame5577"
    _credit_card_loc_value = "//div[@id='root']//input[@name='cardnumber' and @aria-invalid='false']"
    _invalid_cc_no_msg_loc_value = "//span[contains(text(),'Your card number is invalid.')]"
    _exp_date_loc_value = "//div[@id='root']//input[@name='exp-date' and @aria-invalid='false']"
    _cvc_no_loc_value = "//div[@id='root']//input[@name='cvc' and @aria-invalid='false']"
    _postal_code_loc_value = "billingPostalCode"
    # _buy_now_button_loc_value = "//div[@role='none']//span[contains(text(),'Buy Now')]"
    _buy_now_button_loc_value = "//div[@role='none']//button"
    _cc_declined_msg_loc_value = "//li[contains(text(),'The card was declined.')]"
    # Locator types
    _search_course_text_loc_type = "id"
    _search_icon_loc_type = "id"
    _courses_names_loc_type = "class"
    _course_enroll_loc_type = "id"
    _iframe_cc_no_loc_type = "name"
    _iframe_exp_date_loc_type = "name"
    _iframe_cvc_no_loc_type = "name"
    _credit_card_loc_type = "xpath"
    _invalid_cc_no_msg_loc_type = "xpath"
    _exp_date_loc_type = "xpath"
    _cvc_no_loc_type = "xpath"
    _postal_code_loc_type = "id"
    _buy_now_button_loc_type = "xpath"
    _cc_declined_msg_loc_type = "xpath"

    def _search_course(self, course_name):
        self.sendKeys(data=course_name, locator=self._search_course_text_loc_value,
                      locatorType=self._search_course_text_loc_type)
        self._click_search_button()

    def _click_search_button(self):
        self.elementClick(locator=self._search_icon_loc_value, locatorType=self._search_icon_loc_type)



    def _get_search_matching_courses(self):
        self._course_name_elements_list = self.getElementList(locator=self._courses_names_loc_value,
                                                              locatorType=self._courses_names_loc_type)

    def _verify_course_of_choice(self, match_keyword):
        self._course_names = []
        for element in self._course_name_elements_list:
            self._course_names.append(self.getText(element=element, info="matching with '{}'".format(match_keyword)))
        for index, name in enumerate(self._course_names):
            if match_keyword in name:
                self._course_element_to_be_clicked = self._course_name_elements_list[index]
                self.log.info("The full name of the course that needs to be clicked is - {}".format(name))
                break

    def _click_course(self):
        self.elementClick(element=self._course_element_to_be_clicked)

    def _select_course(self, match_keyword):
        self._get_search_matching_courses()
        self._verify_course_of_choice(match_keyword)
        self._click_course()



    def _click_to_enroll_course(self):
        self.elementClick(locator=self._course_enroll_loc_value, locatorType=self._course_enroll_loc_type)



    def _scroll_page(self, direction="down", y_movement=650):
        self.webScroll(direction="up", y_movement=1000)
        self.webScroll(direction=direction, y_movement=y_movement)



    def _enter_cc_number(self, cc_num=_credit_card_no_val):
        # self.switchToFrame(index=0)
        self.switchToFrameByIndex(locator=self._credit_card_loc_value, locatorType=self._credit_card_loc_type)
        self.sendKeys(data=cc_num, locator=self._credit_card_loc_value, locatorType=self._credit_card_loc_type)
        self.switchToDefaultContent()

    def _enter_exp_date(self, date=_valid_thru_date):
        # self.switchToFrame(index=1)
        self.switchToFrameByIndex(locator=self._exp_date_loc_value, locatorType=self._exp_date_loc_type)
        self.sendKeys(data=date, locator=self._exp_date_loc_value, locatorType=self._exp_date_loc_type)
        self.switchToDefaultContent()

    def _enter_cvc_code(self, cvc=_cvv_no):
        # self.switchToFrame(index=2)
        self.switchToFrameByIndex(locator=self._cvc_no_loc_value, locatorType=self._cvc_no_loc_type)
        self.sendKeys(data=cvc, locator=self._cvc_no_loc_value, locatorType=self._cvc_no_loc_type)
        self.switchToDefaultContent()

    def _enter_pin_code(self, pin_code=_postal_code_no):
        self.sendKeys(data=pin_code, locator=self._postal_code_loc_value, locatorType=self._postal_code_loc_type)

    def _check_for_buy_now_button(self):
        result = self.isElementEnabled(locator=self._buy_now_button_loc_value, locatorType=self._buy_now_button_loc_type,
                                       info="Buy Now Button")
        return result

    def _click_buy_now_button(self):
        self.elementClick(locator=self._buy_now_button_loc_value, locatorType=self._buy_now_button_loc_type)



    def _check_for_invalid_card_no(self, cc_num):
        self._enter_cc_number(cc_num=cc_num)
        self._invalid_cc_no_msg_element = self.waitForElement(locator=self._invalid_cc_no_msg_loc_value,
                                                              locatorType=self._invalid_cc_no_msg_loc_type, timeout=5)
        result = self.isElementDisplayed(element=self._invalid_cc_no_msg_element)
        self._register_val_results.append(result)
        self.page_test_status_obj.mark(result, "Invalid Card Message Validation")

    def _check_for_valid_card_no(self, cc_num, val_tru, cvc_no):
        result1 = self._check_for_buy_now_button()
        self._register_val_results.append(not result1)
        self.page_test_status_obj.mark(not result1,
                                       "Checking By Now Button is not enabled before typing in credentials")
        self._enter_cc_number(cc_num)
        self._enter_exp_date(val_tru)
        self._enter_cvc_code(cvc_no)
        self._enter_pin_code(self._postal_code_no)
        time.sleep(2)
        result2 = self._check_for_buy_now_button()
        self._register_val_results.append(result2)
        self.page_test_status_obj.mark(result2, "Valid Card num validation done, by checking for Buy Now button")

    def _check_for_card_declined(self):
        self._click_buy_now_button()
        self._cc_declined_msg_element = self.waitForElement(locator=self._cc_declined_msg_loc_value,
                                                            locatorType=self._cc_declined_msg_loc_type, timeout=10)
        result = self.isElementDisplayed(element=self._cc_declined_msg_element)
        self._register_val_results.append(result)
        self.page_test_status_obj.mark(result, "Card Declined Message Validation")

    # All page level validations holding attribute
    _register_val_results = []


    def register_course(self, course_name=_course_search_name, match_keyword=_keyword_of_interest, cc_num=_credit_card_no_val,
                        val_tru=_valid_thru_date, cvc_no=_cvv_no):
        self._search_course(course_name)
        self._select_course(match_keyword)
        self._click_to_enroll_course()
        self._scroll_page(direction="down", y_movement=650)
        time.sleep(5)
        self._check_for_invalid_card_no(self._credit_card_no_inval)
        time.sleep(5)
        self.driver.refresh()
        self._scroll_page(direction="down", y_movement=750)
        time.sleep(5)
        self._check_for_valid_card_no(cc_num, val_tru, cvc_no)
        time.sleep(5)
        self._check_for_card_declined()
        self._scroll_page(direction="down", y_movement=150)
        time.sleep(5)


