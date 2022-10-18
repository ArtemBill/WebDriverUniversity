import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass





class Test_ButtonClicks(BaseClass):

    # Open Button Links page
    # Click the first button, check the title of the modal window and click Close
    # Click second button, check the title of the modal window and click Close
    # Click third button, check the title of the modal window and click Close
    # Return to the HomePage
    def test_ButtonClicks(self):
        homePage = HomePage(self.driver)
        buttonClicksPage = homePage.openButtonClicksPage()

        buttonClicksPage.clickFirstButton()
        time.sleep(0.5)
        assert "Congratulations!" in buttonClicksPage.getPopupTitleText(), "You didn't open first popup"
        buttonClicksPage.closePopup()

        buttonClicksPage.clickSecondButton()
        time.sleep(0.5)
        assert "It’s that Easy!!" in buttonClicksPage.getPopupTitleText(), "You didn't open second popup"
        buttonClicksPage.closePopup()

        time.sleep(1)
        buttonClicksPage.moveAndClickThirdButton()
        time.sleep(2)
        assert "Well done!" in buttonClicksPage.getPopupTitleText(), "You didn't open third popup"
        buttonClicksPage.closePopup()





