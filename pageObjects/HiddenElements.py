from selenium.webdriver.common.by import By


class HiddenElements:
    def __init__(self, driver):
        self.driver = driver

    firstButton = (By.CSS_SELECTOR, "#not-displayed p")
    secondButton = (By.CSS_SELECTOR, "#button2")
    thirdButton = (By.ID, "button3")

    firstPopup = "//h4[@class='modal-title']"
    secondPopup = "(//h4[@class='modal-title'])[2]"
    thirdPopup = "(//h4[@class='modal-title'])[3]"

    firstPopupButtonClose = (By.XPATH, "//div[@class='modal-footer']/button")
    secondPopupButtonClose = (By.XPATH, "(//div[@class='modal-footer']/button)[2]")
    thirdPopupButtonClose = (By.XPATH, "(//div[@class='modal-footer']/button)[3]")


    def openFirstPopup(self):
        button = self.driver.find_element(*HiddenElements.firstButton)
        self.driver.execute_script("arguments[0].click();", button)

    def openSecondPopup(self):
        button = self.driver.find_element(*HiddenElements.secondButton)
        self.driver.execute_script("arguments[0].click();", button)

    def openThirdPopup(self):
        self.driver.find_element(*HiddenElements.thirdButton).click()



    # def getFirstPopup(self):
    #     return self.driver.find_element(*HiddenElements.firstPopup)




    def getFirstPopupText(self):
        return self.driver.find_element(By.XPATH, HiddenElements.firstPopup).text

    def getSecondPopupText(self):
        return self.driver.find_element(By.XPATH, HiddenElements.secondPopup).text

    def getThirdPopupText(self):
        return self.driver.find_element(By.XPATH, HiddenElements.thirdPopup).text



    def closeFirstPopup(self):
        self.driver.find_element(*HiddenElements.firstPopupButtonClose).click()

    def closeSecondPopup(self):
        self.driver.find_element(*HiddenElements.secondPopupButtonClose).click()

    def closeThirdPopup(self):
        self.driver.find_element(*HiddenElements.thirdPopupButtonClose).click()




