import openpyxl
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ContactUs:
    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "first_name")
    lastname = (By.XPATH, "(//input[@type='text'])[2]")
    email = (By.CSS_SELECTOR, "form input:nth-child(3)")
    comment = (By.TAG_NAME, "textarea")
    submit = (By.XPATH, "//input[@value='SUBMIT']")
    message = (By.XPATH, "//div[@id='contact_reply']/h1")


    def sendName(self, text):
        self.driver.find_element(*ContactUs.name).send_keys(text)

    def sendLastname(self, text):
        self.driver.find_element(*ContactUs.lastname).send_keys(text)

    def sendEmail(self, text):
        self.driver.find_element(*ContactUs.email).send_keys(text)

    def sendComment(self, text):
        self.driver.find_element(*ContactUs.comment).send_keys(text)

    def Submit(self):
        self.driver.find_element(*ContactUs.submit).click()

    def getMessage(self):
        return self.driver.find_element(*ContactUs.message).text


class ContactUsExcel(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.sheet = self.getExcelActiveSheet()

    def sendNameFromExcel(self, text):
        self.driver.find_element(*ContactUs.name).send_keys(self.sheet[text].value)

    def sendLastnameFromExcel(self, text):
        self.driver.find_element(*ContactUs.lastname).send_keys(self.sheet[text].value)

    def sendEmailFromExcel(self, text):
        self.driver.find_element(*ContactUs.email).send_keys(self.sheet[text].value)

    def sendCommentFromExcel(self, text):
        self.driver.find_element(*ContactUs.comment).send_keys(self.sheet[text].value)



