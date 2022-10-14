import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DropdownMenu:
    def __init__(self, driver):
        self.driver = driver

    # Dropdown
    dropdown1 = (By.CSS_SELECTOR, "#dropdowm-menu-1")
    dropdown2 = (By.CSS_SELECTOR, "#dropdowm-menu-2")
    elemInDropdown2 = (By.XPATH, "//select[@id='dropdowm-menu-2']/option")
    dropdown3 = (By.CSS_SELECTOR, "#dropdowm-menu-3")

    # Checkboxes
    checkboxes = (By.CSS_SELECTOR, "div[id='checkboxes'] label")
    checkboxInput = (By.TAG_NAME, "input")

    # Radio Buttons
    radioButtons = (By.XPATH, "(//form[@class='radio-buttons'])[1]")
    radioButtonInputs = (By.XPATH, "//input[@name='color']")

    # Selected & Disabled
    disabledElem = (By.XPATH, "//form[@id='radio-buttons-selected-disabled']/input[@value='cabbage']")
    vegetable = (By.XPATH, "//form[@id='radio-buttons-selected-disabled']")
    elemInputs = (By.XPATH, "//input[@name='vegetable']")
    dropdown4 = (By.CSS_SELECTOR, "#fruit-selects")


    # Dropdown
    def selectFromDropdown1ByText(self, elem):
        dropdown = Select(self.driver.find_element(*DropdownMenu.dropdown1))
        dropdown.select_by_visible_text(elem)
        self.checkDropdown1Value(elem)

    def selectFromDropdown2ByIndex(self, index):
        dropdown = Select(self.driver.find_element(*DropdownMenu.dropdown2))
        dropdown.select_by_index(index)
        self.checkDropdown2Value(index)

    def selectFromDropdown3ByValue(self, value):
        dropdown = Select(self.driver.find_element(*DropdownMenu.dropdown3))
        dropdown.select_by_value(value)
        self.checkDropdown3Value(value)



    def getDropdown1Value(self):
        return self.driver.find_element(*DropdownMenu.dropdown1).get_attribute("value")

    def checkDropdown1Value(self, elem):
        assert elem.lower() == self.getDropdown1Value()



    def getDropdown2Value(self):
        return self.driver.find_element(*DropdownMenu.dropdown2).get_attribute("value")

    def checkDropdown2Value(self, index):
        dropdown2Value = self.driver.find_elements(*DropdownMenu.elemInDropdown2)
        elemValue = []
        for elem in dropdown2Value:
            elemValue.append(elem.text)
        assert elemValue[index].lower() == self.getDropdown2Value()



    def getDropdown3Value(self):
        return self.driver.find_element(*DropdownMenu.dropdown3).get_attribute("value")

    def checkDropdown3Value(self, value):
        assert value == self.getDropdown3Value()




    # Checkboxes
    def getCheckboxes(self):
        return self.driver.find_elements(*DropdownMenu.checkboxes)

    def selectCheckboxes(self, testCheckboxes):
        test_checkboxes = testCheckboxes
        for checkbox in self.getCheckboxes():
            if checkbox.text in test_checkboxes:
                if not checkbox.find_element(*DropdownMenu.checkboxInput).is_selected():
                    checkbox.click()
                    assert checkbox.find_element(*DropdownMenu.checkboxInput).is_selected()
            else:
                if checkbox.find_element(*DropdownMenu.checkboxInput).is_selected():
                    checkbox.click()




    # Radio Buttons
    # Take elements text and make a list
    def getRadioButtonsValue(self):
        radioButtonsValue = self.driver.find_element(*DropdownMenu.radioButtons).text
        return [i for i in radioButtonsValue.split()]

    def getRadioButtonInputs(self):
        return self.driver.find_elements(*DropdownMenu.radioButtonInputs)

    # find right elem by index and click same index input
    def selectRadioButton(self, testRadioButton):
        radioButtonsValue = self.getRadioButtonsValue()
        inputs = self.getRadioButtonInputs()
        for i in range(len(radioButtonsValue)):
            if radioButtonsValue[i] == testRadioButton:
                for k in range(len(inputs)):
                    if k == i:
                        # print(inputs[k])
                        inputs[k].click()
                        assert inputs[k].is_selected()
                        return



    # Selected & Disabled
    # RadioButtons
    def checkDisabledElem(self):
        assert not self.driver.find_element(*DropdownMenu.disabledElem).is_enabled()

    def getVegetableElem(self):
        elements = self.driver.find_element(*DropdownMenu.vegetable).text
        return [i for i in elements.split()]

    def getSelectedAndDisabledInputs(self):
        return self.driver.find_elements(*DropdownMenu.elemInputs)

    def selectVegetable(self, testVegetable):
        vegetables = self.getVegetableElem()
        inputs = self.getSelectedAndDisabledInputs()
        for i in range(len(vegetables)):
            if vegetables[i] == testVegetable:
                for k in range(len(inputs)):
                    if k == i:
                        inputs[k].click()
                        assert inputs[k].is_selected()
                        return

    #dropdown
    def selectFromDropdown4ByText(self, elem):
        dropdown = Select(self.driver.find_element(*DropdownMenu.dropdown4))
        dropdown.select_by_visible_text(elem)
        self.checkDropdown4Value(elem)

    def getDropdown4Value(self):
        return self.driver.find_element(*DropdownMenu.dropdown1).get_attribute("value")

    def checkDropdown4Value(self, elem):
        assert elem.lower() == self.getDropdown4Value()



