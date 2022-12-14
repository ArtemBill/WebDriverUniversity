import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class Test_FileUpload(BaseClass):

    # Upload file and check text in alert
    def test_FileUpload(self):
        homePage = HomePage(self.driver)
        fileUploadPage = homePage.openFileUploadPage()

        # Local path
        imagePath = "/Users/soprano/Desktop/PetProject/files/icon.png"

        fileUploadPage.uploadFile(imagePath)
        fileUploadPage.Submit()
        alerText = "Your file has now been uploaded!"
        self.checkAlertText(alerText)



