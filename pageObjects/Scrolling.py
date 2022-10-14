from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Scrolling:
    def __init__(self, driver):
        self.driver = driver


    elem1 = (By.XPATH, "//div[@id='zone1']")
    elem2 = (By.ID, "zone2")
    elem3 = (By.ID, "zone3")
    elem4 = (By.ID, "zone4")

    def moveTo(self, elem, text):
        action = ActionChains(self.driver)
        action.move_to_element(elem).perform()
        assert text in elem.text

    def scrollToElem1AndCheckText(self, text):
        self.moveTo(self.driver.find_element(*Scrolling.elem1), text)

    def scrollToElem2AndCheckText(self, text):
        self.moveTo(self.driver.find_element(*Scrolling.elem2), text)

    def scrollToElem3AndCheckText(self, text):
        self.moveTo(self.driver.find_element(*Scrolling.elem3), text)

    def scrollToElem4AndCheckText(self, text):
        self.moveTo(self.driver.find_element(*Scrolling.elem4), text)
