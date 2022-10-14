from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_Scrolling(BaseClass):

    # Open Scrolling Page
    # Grab the text of 1st element
    # Scroll and move to 2nd and 3rd elements. Grab their text
    # Scroll and move to 4th elements. Grab its text
    def test_Scrolling(self):
        homePage = HomePage(self.driver)
        scrollingPage = homePage.openScrollingPage()


        # 1st elem
        scrollingPage.scrollToElem1AndCheckText("Well done for scrolling to me!")

        # 2nd and 3rd elements
        self.driver.execute_script("window.scrollTo(0,250)")

        scrollingPage.scrollToElem2AndCheckText("1")
        scrollingPage.scrollToElem3AndCheckText("1")

        scrollingPage.scrollToElem2AndCheckText("2")
        scrollingPage.scrollToElem3AndCheckText("2")


        # 4th element
        self.driver.execute_script("window.scrollTo(0,480)")

        scrollingPage.scrollToElem4AndCheckText("X:" and "Y:")


