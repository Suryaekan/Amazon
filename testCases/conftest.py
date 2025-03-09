import os
from datetime import datetime
import pytest
from selenium import webdriver

@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
        print("Launching Edge")
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        print("Launching Firefox")
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        print("Launching Chrome")

    request.cls.driver = driver  # Attach the driver to the test class
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(report_dir, exist_ok=True)  # Create the directory if it doesn't exist
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    config.option.htmlpath = os.path.join(report_dir, f"Test_Report_{timestamp}.html")
