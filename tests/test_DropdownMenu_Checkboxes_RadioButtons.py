from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class Test_DropdownMenu(BaseClass):

    # Open Dropwdown Menu, Checkboxes, and Radio Buttons page
    # Choose Python, JUnit and CSS in Dropdown Menu
    # Select checkboxes from test_checkboxes
    # Select Purple Radio Button
    # Select Lettuce in Selected and Disabled. Make sure Cabbage is not available
    def test_DropdownMenu(self):
        homePage = HomePage(self.driver)
        dropdownMenuPage = homePage.openDropdownMenuPage()


        # Dropdown
        dropdownMenuPage.selectFromDropdown1ByText("Python")
        dropdownMenuPage.selectFromDropdown2ByIndex(3)
        dropdownMenuPage.selectFromDropdown3ByValue("css")

        # Checkboxes
        testCheckboxes = {"Option 1", "Option 4"}
        dropdownMenuPage.selectCheckboxes(testCheckboxes)

        # Radio Buttons
        dropdownMenuPage.selectRadioButton("Orange")

        # Selected & Disabled
        dropdownMenuPage.checkDisabledElem()
        dropdownMenuPage.selectVegetable("Lettuce")

