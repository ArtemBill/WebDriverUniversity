from selenium.webdriver import ActionChains
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_Actions(BaseClass):

    # open Actions page
    # drag one elem to another
    # double click elem
    # mousehover 3 buttons, click dropdown links and check popup text
    # hold button and check its text
    def test_Actions(self):
        homePage = HomePage(self.driver)
        actionsPage = homePage.openActionsPage()

        action = ActionChains(self.driver)

        # drag and drop
        elemToDrag = actionsPage.getDraggableElem()
        elemToDrop = actionsPage.getDroppableElem()
        action.drag_and_drop(elemToDrag, elemToDrop).perform()


        # double-click
        action.double_click(actionsPage.getDoubleClickElem()).perform()


        # mousehover
        # 1st button
        action.move_to_element(actionsPage.getMoveToFirstElem()).perform()
        actionsPage.clickFirstDropdownLink_1()
        alertText = "Well done"
        self.checkAlertText(alertText)

        # 2nd button
        action.move_to_element(actionsPage.getMoveToSecondElem()).perform()
        actionsPage.clickSecondDropdownLink_1()
        self.checkAlertText(alertText)

        # 3rd button 1st link
        action.move_to_element(actionsPage.getMoveToThirdElem()).perform()
        actionsPage.clickThirdDropdownLink_1()
        self.checkAlertText(alertText)

        # 3rd button 2nd link
        action.move_to_element(actionsPage.getMoveToThirdElem()).perform()
        actionsPage.clickThirdDropdownLink_2()
        self.checkAlertText(alertText)


        # holding button
        actionsPage.holdElemAndCheckText()


