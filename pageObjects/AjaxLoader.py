from selenium.webdriver.common.by import By


class AjaxLoader:
    def __init__(self, driver):
        self.driver = driver

    button = "//span[@type='button']"
    modalTitle = "//h4[@class='modal-title']"


    def getButton(self):
        return AjaxLoader.button

    def clickButton(self):
        self.driver.find_element(By.XPATH, AjaxLoader.button).click()

    def getModalTitle(self):
        return self.driver.find_element(By.XPATH, AjaxLoader.modalTitle)

    def getModalTitleText(self):
        modalTitleText = self.driver.find_element(By.XPATH, AjaxLoader.modalTitle).text
        return modalTitleText
