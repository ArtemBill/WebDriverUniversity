from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_LoginPortal(BaseClass):

    # Open Login Portal page
    # Enter username and password. Click Login
    # Check text in alert popup and click OK
    # Return to the HomePage
    def test_LoginPortal(self):
        homePage = HomePage(self.driver)
        loginPortalPage = homePage.openLoginPortalPage()

        loginPortalPage.login("Artem")
        loginPortalPage.password("artem99")
        loginPortalPage.submit()
        self.checkAlertText("validation failed")

