import time
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_ToDoList(BaseClass):

    # Open To Do List page
    # delete the first item and check if it ids removed
    # add the deleted item and check if it is added
    # Return to the HomePage
    def test_ToDoList(self):
        homePage = HomePage(self.driver)
        toDoListPage = homePage.openToDoListPage()


        item1Text = toDoListPage.getItem1Text()
        toDoListPage.deleteItem1()
        time.sleep(1)
        assert item1Text not in toDoListPage.getItem1Text()
        toDoListPage.addNewItem(item1Text)
        toDoListPage.checkLastItemText(item1Text)
