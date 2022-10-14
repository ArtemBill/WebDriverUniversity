import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Actions:
    def __init__(self, driver):
        self.driver = driver

    # drag and drop
    elemToDrag = (By.CSS_SELECTOR, "#draggable")
    elemToDrop = (By.CSS_SELECTOR, "#droppable")

    # double-click
    elem_to_doubleClick = (By.CSS_SELECTOR, "#double-click")


    # mousehover
    # 1st button
    moveToFirstElem = (By.XPATH, "(//div[@id='div-hover']/div/button)[1]")
    firstDropdownLink_1 = (By.CLASS_NAME, "dropdown-content")

    # 2nd button
    moveToSecondElem = (By.XPATH, "(//div[@id='div-hover']/div/button)[2]")
    secondDropdownLink_1 = (By.XPATH, "(//div[@class='dropdown-content'])[2]")

    # 3rd button 1st link
    moveToThirdElem = (By.XPATH, "(//div[@id='div-hover']/div/button)[3]")
    thirdDropdownLink_1 = (By.XPATH, "((//div[@class='dropdown-content'])[3]/a)[1]")
    thirdDropdownLink_2 = (By.XPATH, "((//div[@class='dropdown-content'])[3]/a)[2]")


    # keep holding
    elemToHold = (By.CSS_SELECTOR, "#click-box")


    # drag and drop
    def getDraggableElem(self):
        elem = self.driver.find_element(*Actions.elemToDrag)
        return elem

    def getDroppableElem(self):
        elem = self.driver.find_element(*Actions.elemToDrop)
        return elem


    # double-click
    def getDoubleClickElem(self):
        elem = self.driver.find_element(*Actions.elem_to_doubleClick)
        return elem



    # mousehover
    def getMoveToFirstElem(self):
        elem = self.driver.find_element(*Actions.moveToFirstElem)
        return elem

    def clickFirstDropdownLink_1(self):
        self.driver.find_element(*Actions.firstDropdownLink_1).click()

    def getMoveToSecondElem(self):
        elem = self.driver.find_element(*Actions.moveToSecondElem)
        return elem

    def clickSecondDropdownLink_1(self):
        self.driver.find_element(*Actions.secondDropdownLink_1).click()

    def getMoveToThirdElem(self):
        elem = self.driver.find_element(*Actions.moveToThirdElem)
        return elem

    def clickThirdDropdownLink_1(self):
        self.driver.find_element(*Actions.thirdDropdownLink_1).click()

    def clickThirdDropdownLink_2(self):
        self.driver.find_element(*Actions.thirdDropdownLink_2).click()


    # keep holding
    def holdElemAndCheckText(self):
        elem = self.driver.find_element(*Actions.elemToHold)
        action = ActionChains(self.driver)
        action.move_to_element(elem).click_and_hold().perform()
        time.sleep(1)
        assert "keep holding" in elem.text