import time
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_Popup_Alerts(BaseClass):

    # Open Popup & Alerts Page
    # Open JS Alert and check text
    # Open Modal Popup and check text
    # Wait for next modal popup and check text
    # Open JS Alert, choose accept and cancel, checking the text under 'click me' button
    def test_Popup_Alerts(self):
        homePage = HomePage(self.driver)
        popupAlertsPage = homePage.openPopupAlertsPage()


        # JS Alert
        popupAlertsPage.openPopup1()
        time.sleep(0.5)
        alertText = "I am an alert box!"
        self.checkAlertText(alertText)

        # Modal Popup
        popupAlertsPage.openPopup2()
        time.sleep(0.5)
        text = "It’s that Easy!!"
        popupAlertsPage.checkPopupText(text)

        # Ajax Loader
        popupAlertsPage.openPopup3()
        time.sleep(0.5)
        self.waitForClickable(popupAlertsPage.ajaxLoaderButton)
        popupAlertsPage.clickAjaxLoaderButton()
        time.sleep(0.5)
        text = "Well Done For Waiting"
        popupAlertsPage.checkPopupText(text)
        time.sleep(0.5)
        self.driver.back()

        # JS Confirm popup
        popupAlertsPage.openPopup4()
        time.sleep(0.5)
        alertText = "Press a button!"
        self.checkAlertText(alertText)
        confirmAlertText = "You pressed OK!"
        popupAlertsPage.checkConfirmAlertText(confirmAlertText)

        popupAlertsPage.openPopup4()
        time.sleep(0.5)
        alert = self.driver.switch_to.alert
        alertText = alert.text
        assert "Press a button!" in alertText
        alert.dismiss()
        confirmAlertText = "You pressed Cancel!"
        popupAlertsPage.checkConfirmAlertText(confirmAlertText)


