from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ToDoList:
    def __init__(self, driver):
        self.driver = driver


    item1 = (By.CSS_SELECTOR, "ul li:nth-child(1)")
    item1DeleteButton = (By.CSS_SELECTOR, "ul li:nth-child(1) i")
    entryField = (By.XPATH, "//input[@type='text']")
    itemList = (By.CSS_SELECTOR, "ul li")


    def getItem1Text(self):
        return self.driver.find_element(*ToDoList.item1).text

    def deleteItem1(self):
        self.driver.find_element(*ToDoList.item1DeleteButton).click()

    def addNewItem(self, text):
        self.driver.find_element(*ToDoList.entryField).send_keys(text)
        self.driver.find_element(*ToDoList.entryField).send_keys(Keys.ENTER)

    def getItemList(self):
        return self.driver.find_elements(*ToDoList.itemList)

    def checkLastItemText(self, text):
        items = self.driver.find_elements(*ToDoList.itemList)
        for item in items:
            if item == items[-1]:
                assert item.text == text, "maybe, you didn't add deleted item"






