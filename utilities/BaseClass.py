import openpyxl
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("setup")
class BaseClass:


    def waitForVisibility(self, element):
        wait = WebDriverWait(self.driver, 10).until\
            (EC.visibility_of_element_located((By.XPATH, element)))

    def waitForClickable(self, element):
        WebDriverWait(self.driver, 10).until\
            (EC.element_to_be_clickable((By.XPATH, element)))

    def getExcelActiveSheet(self):
        book = openpyxl.load_workbook("/Users/soprano/Desktop/PetProject/files/contacts.xlsx")
        return book.active

    def checkAlertText(self, text):
        alert = self.driver.switch_to.alert
        alertText = alert.text
        assert text in alertText
        alert.accept()