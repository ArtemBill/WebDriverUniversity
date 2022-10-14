from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_PageObjectModel(BaseClass):

    # Open Page Object Model
    # Open Our Products Tab
    # check popup text in each category
    # Return to the HomePage
    def test_PageObjectModel(self):
        homePage = HomePage(self.driver)
        pageObjectModel = homePage.openPageObjectModelPage()

        pageObjectModel.openProducts()
        pageObjectModel.checkPopupText("SPECIAL OFFER!")


