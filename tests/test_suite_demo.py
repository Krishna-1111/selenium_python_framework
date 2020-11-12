import unittest
from tests.courses_test.register_courses_csv_data_test import RegisterCoursesCSVDataTests
from tests.home_test.login_tests import LoginTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
