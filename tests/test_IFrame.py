from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_IFrame(BaseClass):

    # Open Page Object Model
    # Open Our Products Tab
    # check popup text in each category
    # Return to the HomePage
    def test_IFrame(self):
        homePage = HomePage(self.driver)
        iframePage = homePage.openIframePage()

        iframePage.openProducts()
        iframePage.checkPopupText("SPECIAL OFFER!")





