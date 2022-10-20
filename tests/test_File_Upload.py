import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class Test_FileUpload(BaseClass):

    # Upload file and check text in alert
    def test_FileUpload(self):
        homePage = HomePage(self.driver)
        fileUploadPage = homePage.openFileUploadPage()

        # Local path
        # imagePath = "/Users/soprano/Desktop/PetProject/files/icon.png"

        # Git repo path
        imagePath = "/home/ubuntu/imgs/icon.png"
        fileUploadPage.uploadFile(imagePath)
        fileUploadPage.Submit()
        time.sleep(4)
        alerText = "Your file has now been uploaded!"
        self.checkAlertText(alerText)



