import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    # This code for running on remote machine.
    options = Options()
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)

    # This code for local testing
    # s = Service("/Users/soprano/Desktop/First_Module/pythonSelenium/chromedriver")
    # driver = webdriver.Chrome(service=s)

    driver.implicitly_wait(10)
    driver.get("http://webdriveruniversity.com/index.html")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    HomePage_header = driver.find_element(By.CSS_SELECTOR, "#udemy-promo-thumbnail h1").text
    assert "My Courses & Promo Codes" in HomePage_header, "Maybe, You're not at Home Page"
    driver.close()