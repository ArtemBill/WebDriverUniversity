from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_HiddenElements(BaseClass):

    # Open Hidden Elements Page
    # JS Click first and second button. Check popups
    # check the last popup
    def test_HiddenElements(self):
        homePage = HomePage(self.driver)
        hiddenElementsPage = homePage.openHiddenElementsPage()


        hiddenElementsPage.openFirstPopup()
        self.waitForVisibility(hiddenElementsPage.firstPopup)
        assert "Congratulations!" in hiddenElementsPage.getFirstPopupText()
        hiddenElementsPage.closeFirstPopup()


        hiddenElementsPage.openSecondPopup()
        self.waitForVisibility(hiddenElementsPage.secondPopup)
        assert "It’s that Easy!!" in hiddenElementsPage.getSecondPopupText()
        hiddenElementsPage.closeSecondPopup()


        hiddenElementsPage.openThirdPopup()
        self.waitForVisibility(hiddenElementsPage.thirdPopup)
        assert "Well done!" in hiddenElementsPage.getThirdPopupText()
        hiddenElementsPage.closeThirdPopup()


