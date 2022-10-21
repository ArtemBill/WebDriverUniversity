import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    # options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # This code we need for local testing
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