from selenium.webdriver.common.by import By


class LoginPortal:
    def __init__(self, driver):
        self.driver = driver


    loginField = (By.CSS_SELECTOR, "[placeholder='Username']")
    passwordField = (By.CSS_SELECTOR, "form input:nth-child(2)")
    button = (By.CSS_SELECTOR, "#login-button")

    def login(self, text):
        self.driver.find_element(*LoginPortal.loginField).send_keys(text)

    def password(self, text):
        self.driver.find_element(*LoginPortal.passwordField).send_keys(text)

    def submit(self):
        self.driver.find_element(*LoginPortal.button).click()

