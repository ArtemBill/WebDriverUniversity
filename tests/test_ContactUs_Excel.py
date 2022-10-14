from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_ContactUs_Excel(BaseClass):

    # Open Contact Us page
    # Enter First and Last name, email and comment from Excel table. Click Submit
    # Get 'Thank You' message
    # Return to the HomePage
    def test_ContactUs_Excel(self):
        homePage = HomePage(self.driver)
        contactUsExcelPage = homePage.openContactUsExcelPage()
        contactUsPage = homePage.openContactUsPage()

        contactUsExcelPage.sendNameFromExcel("B3")
        contactUsExcelPage.sendLastnameFromExcel("C3")
        contactUsExcelPage.sendEmailFromExcel("D3")
        contactUsExcelPage.sendCommentFromExcel("E3")
        contactUsPage.Submit()
        assert "Thank You" in contactUsPage.getMessage(), "You did something wrong"




