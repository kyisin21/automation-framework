
# Pytest configuration file


import pytest
from datetime import datetime

def pytest_addoption(parser):
    
    # Add command line options for pytest
    
    parser.addoption("--browser", action="store", default="chrome", help="Specify browser for tests")
    parser.addoption("--headless", action="store_true", default=True, help="Run browser in headless mode")

@pytest.fixture(scope="session")
def browser(request):
    
    # Get browser from command line option
    
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def headless(request):
    
    # Get headless mode from command line option
    
    return request.config.getoption("--headless")

def pytest_configure(config):
    
    # Configure pytest
    
    # Configure HTML report
    config.option.htmlpath = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    
    # Set HTML report title
    
    report.title = "Automation Framework Test Report"

@pytest.fixture(autouse=True)
def log_test_name(request):
    
    # Log test name before and after each test
    
    test_name = request.node.name
    print(f"\n========== Starting Test: {test_name} ==========")
    yield
    print(f"\n========== Completed Test: {test_name} ==========")