from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_Ajax_Loader(BaseClass):

    # open AjaxLoader page
    # Wait for loading button
    # click button and check popup text
    def test_Ajax_Loader(self):
        homePage = HomePage(self.driver)
        ajaxLoaderPage = homePage.openAjaxLoaderPage()

        self.waitForClickable(ajaxLoaderPage.getButton())
        ajaxLoaderPage.clickButton()
        self.waitForVisibility(ajaxLoaderPage.modalTitle)
        assert "Well Done For Waiting....!!!" in ajaxLoaderPage.getModalTitleText()



