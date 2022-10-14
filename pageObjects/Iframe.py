from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class Iframe(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    productsButtonOpen = (By.LINK_TEXT, "Our Products")
    categories = (By.CSS_SELECTOR, "[class='sub-heading']")
    popup = "//h4[@class='modal-title']"
    popupButtonClose = (By.XPATH, "(//div[@class='modal-footer']/button)[1]")

    def openProducts(self):
        self.driver.find_element(*Iframe.productsButtonOpen).click()

    def getCategories(self):
        return self.driver.find_elements(*Iframe.categories)

    def getPopupText(self):
        return self.driver.find_element(By.XPATH, Iframe.popup).text

    def closePopup(self):
        self.driver.find_element(*Iframe.popupButtonClose).click()

    def checkPopupText(self, text):
        categories = self.getCategories()
        for category in categories:
            category.click()
            self.waitForVisibility(Iframe.popup)
            assert text in self.getPopupText()
            self.closePopup()



