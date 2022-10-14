from selenium.webdriver.common.by import By


class DatePicker:
    def __init__(self, driver):
        self.driver = driver

    calendarButton = (By.CSS_SELECTOR, "span[class='input-group-addon']")
    monthSelectionMenu = (By.XPATH, "(//th[@colspan='5'])[1]")
    yearSelectionMenu = (By.XPATH, "(//th[@colspan='5'])[2]")
    actualYearsLocators = (By.XPATH, "//div[@class='datepicker-years']/table/tbody/tr/td/span")
    monthLocators = (By.CSS_SELECTOR, "span[class*='month']")
    daysLocators = (By.XPATH, "//div[@class='datepicker-days']/table/tbody/tr/td")
    switchNext = (By.XPATH, "//div[@class='datepicker-years']/table/thead/tr/th[@class='next']")
    switchPrev = (By.XPATH, "//div[@class='datepicker-years']/table/thead/tr/th[@class='prev']")
    dateField = (By.CSS_SELECTOR, "input[type='text']")

    def openCalendar(self):
        self.driver.find_element(*DatePicker.calendarButton).click()

    def openMonthSelectionMenu(self):
        self.driver.find_element(*DatePicker.monthSelectionMenu).click()

    def openYearSelectionMenu(self):
        self.driver.find_element(*DatePicker.yearSelectionMenu).click()

    def getActualYearsChoice(self):
        return self.driver.find_elements(*DatePicker.actualYearsLocators)

    def getMonthChoice(self):
        return self.driver.find_elements(*DatePicker.monthLocators)

    def getDaysChoice(self):
        return self.driver.find_elements(*DatePicker.daysLocators)

    def getDataFieldValue(self):
        return self.driver.find_element(*DatePicker.dateField).get_attribute("value")

    def SwitchNext(self):
        self.driver.find_element(*DatePicker.switchNext).click()

    def SwitchPrev(self):
        self.driver.find_element(*DatePicker.switchPrev).click()

    def chooseYear(self, testYear):
        while True:
            yearLocators = self.getActualYearsChoice()
            yearsData = set()

            for yearLocator in yearLocators:
                if int(yearLocator.text) == testYear:
                    yearLocator.click()
                    return
                yearsData.add(int(yearLocator.text))

            if testYear < min(yearsData):
                self.SwitchPrev()
            if testYear > max(yearsData):
                self.SwitchNext()

    def chooseMonth(self, testMonth):
        months = self.getMonthChoice()
        for month in months:
            if month.text == testMonth:
                month.click()
                break

    def chooseDay(self, testDay):
        days = self.getDaysChoice()
        for day in days:
            if int(day.text) == testDay:
                day.click()
                break

    def checkData(self, testData):
        assert testData == self.getDataFieldValue()