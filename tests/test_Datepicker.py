from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class Test_Datepicker(BaseClass):

    # choose date 05.26.1995
    def test_Datepicker(self):
        homePage = HomePage(self.driver)
        datePickerPage = homePage.openDatePickerPage()

        datePickerPage.openCalendar()
        datePickerPage.openMonthSelectionMenu()
        datePickerPage.openYearSelectionMenu()

        datePickerPage.chooseYear(1995)
        datePickerPage.chooseMonth("May")
        datePickerPage.chooseDay(26)
        datePickerPage.checkData("05-26-1995")



