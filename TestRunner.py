import os
from unittest import TestLoader, TestSuite
from Tests.LoginTests import LoginTest
from Tests.SearchTest import SearchTest
from Tests.ProductTests import ProductTest
from pyunitreport import HTMLTestRunner
from datetime import datetime

if __name__ == "__main__":

    test_loader = TestLoader()

    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(LoginTest),
        test_loader.loadTestsFromTestCase(SearchTest),
        test_loader.loadTestsFromTestCase(ProductTest)


    ))

    # Creating output directory if not exists
    reports = '{}\\reports'.format(os.path.dirname(os.path.abspath(__file__)))
    try:
        if not os.path.exists(reports):
            os.makedirs(reports)
    except OSError as e:
        print("Couldn't create output directory, Error: {}".format(e))

    # Creating a html results file
    kwargs = {
        "output": reports,
        "report_name": "report_{}.html".format(datetime.now().strftime("%d-%m-%Y-%H-%M-%S")),
        "failfast": True
    }
    runner = HTMLTestRunner(**kwargs)
    runner.run(test_suite)
