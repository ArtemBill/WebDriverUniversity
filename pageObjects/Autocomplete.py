from selenium.webdriver.common.by import By


class Autocomplete:
    def __init__(self, driver):
        self.driver = driver

    textInput = (By.NAME, "food-item")
    products = (By.XPATH, "//div[@class='autocomplete-items']/div")
    submit = (By.CSS_SELECTOR, "#submit-button")

    def enterText(self, text):
        self.driver.find_element(*Autocomplete.textInput).send_keys(text)

    def getProductList(self):
        return self.driver.find_elements(*Autocomplete.products)

    def getEnteredText(self):
        return self.driver.find_element(*Autocomplete.textInput).get_attribute("value")

    def Submit(self):
        self.driver.find_element(*Autocomplete.submit).click()