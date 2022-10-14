from selenium.webdriver.common.by import By


class FileUpload:
    def __init__(self, driver):
        self.driver = driver

    fileField = (By.ID, "myFile")
    submit = (By.ID, "submit-button")

    def uploadFile(self, file):
        self.driver.find_element(*FileUpload.fileField).send_keys(file)

    def Submit(self):
        self.driver.find_element(*FileUpload.submit).click()
