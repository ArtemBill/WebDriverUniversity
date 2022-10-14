from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ButtonClicks:
    def __init__(self, driver):
        self.driver = driver

    firstButton = (By.XPATH, "//span[@id='button1']")
    secondButton = (By.CSS_SELECTOR, "[id='button2']")
    thirdButton = (By.XPATH, "//span[@id='button3']")
    popup = (By.CSS_SELECTOR, "[class='modal fade in show'] div div div[class='modal-header'] h4")
    closePopupButton = (By.CSS_SELECTOR, "[class='modal fade in show'] div div div[class='modal-footer'] button")



    def clickFirstButton(self):
        self.driver.find_element(*ButtonClicks.firstButton).click()

    def clickSecondButton(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*ButtonClicks.secondButton))

    def moveAndClickThirdButton(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*ButtonClicks.thirdButton)).click().perform()

    def getPopupTitleText(self):
        return self.driver.find_element(*ButtonClicks.popup).text

    def closePopup(self):
        self.driver.find_element(*ButtonClicks.closePopupButton).click()

