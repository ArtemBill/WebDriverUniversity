from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_ContactUs(BaseClass):

    # Open Contact Us page
    # Enter First and Last name, email and comment. Click Submit
    # Get 'Thank You' message
    # Return to the HomePage
    def test_ContactUs(self):
        homePage = HomePage(self.driver)
        contactUsPage = homePage.openContactUsPage()

        contactUsPage.sendName("Artem")
        contactUsPage.sendLastname("Bilyk")
        contactUsPage.sendEmail("valhalla@gmail.com")
        contactUsPage.sendComment("I am a bad guy")
        contactUsPage.Submit()
        message = contactUsPage.getMessage()
        assert "Thank You" in message, "You did something wrong"


