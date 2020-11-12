import pytest
import utilities.custom_logger as cl
import logging
from base.webdriverfactory import WebDriverFactory
from pages.home_page.login_page import LoginPage


# log = cl.customLogger(logging.DEBUG)
# log = cl.customLogger(logging.DEBUG, file_name="automation_exercise")
# log = cl.customLogger(logging.DEBUG, file_name="automation_exercise_ddt")
# log = cl.customLogger(logging.DEBUG, file_name="automation_exercise_ddt_csv")
log = cl.customLogger(logging.DEBUG, file_name="automation_test_suite")


@pytest.yield_fixture()
def setUp():
    log.info("Running method level setUp ===============================================")
    yield
    log.info("Running method level tearDown ============================================")


@pytest.yield_fixture(scope="class", autouse=True)
def oneTimeSetUp(request, browser, osType):
    log.info("Running one time setUp")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    # login_page_obj = LoginPage(driver)
    # login_page_obj.login("test@email.com", "abcabc")

    if browser == 'firefox':
        log.info("Running tests on <<<<<< FireFox >>>>>>")
        log.info("<<<<< Tests running in {} OS Platform >>>>>".format(osType))
    elif browser == 'chrome':
        log.info("Running tests on <<<<<< Chrome >>>>>>")
        log.info("<<<<< Tests running in {} OS Platform >>>>>".format(osType))
    elif browser == 'iexplorer':
        log.info("Running tests on <<<<<< Internet Explorer >>>>>>")
        log.info("<<<<< Tests running in {} OS Platform >>>>>".format(osType))
    else:
        log.info("Running tests on <<<<<< Chrome >>>>>>")
        log.info("<<<<< Tests running in {} OS Platform >>>>>".format(osType))

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    log.info("Running one time tearDown")
    log.info("End--------------------------------------------------------------------------------------------")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")