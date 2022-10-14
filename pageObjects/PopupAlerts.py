from selenium.webdriver.common.by import By


class PopupAlerts:
    def __init__(self, driver):
        self.driver = driver

    button1 = (By.CSS_SELECTOR, "#button1")
    button2 = (By.ID, "button2")
    button3 = (By.CSS_SELECTOR, "#button3")
    button4 = (By.ID, "button4")

    ajaxLoaderButton = "//span[@id='button1']"
    modalPopup = (By.CSS_SELECTOR, "[class='modal-header'] h4")
    popupButtonClose = (By.XPATH, "//div[@class='modal-footer']/button")
    confirmAlertText = (By.CSS_SELECTOR, "#confirm-alert-text")

    def openPopup1(self):
        self.driver.find_element(*PopupAlerts.button1).click()

    def openPopup2(self):
        self.driver.find_element(*PopupAlerts.button2).click()

    def openPopup3(self):
        self.driver.find_element(*PopupAlerts.button3).click()

    def openPopup4(self):
        self.driver.find_element(*PopupAlerts.button4).click()



    def clickAjaxLoaderButton(self):
        self.driver.find_element(By.XPATH, PopupAlerts.ajaxLoaderButton).click()

    def checkPopupText(self, text):
        modalPopupText = self.driver.find_element(*PopupAlerts.modalPopup).text
        assert text in modalPopupText
        self.driver.find_element(*PopupAlerts.popupButtonClose).click()

    def checkConfirmAlertText(self, text):
        confirmText = self.driver.find_element(*PopupAlerts.confirmAlertText).text
        assert text in confirmText





