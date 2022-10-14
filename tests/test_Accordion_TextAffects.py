from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_Accordion_TestAffects(BaseClass):

    # Open Accordion & text affects page
    # check text visibility change by clicking on element
    def test_Accordion_TextAffects(self):
        homePage = HomePage(self.driver)
        accordionTextAffectsPage = homePage.openAccordionTextAffectsPage()


        blockTestData = {"Manual Testing": "Manual testing has for some time been the most popular way to test code. For this method, the tester plays an important role of end user and verifies that all the features of the application work correctly. Manual testing however is on the decline. Companies and developers have realised the efficiency, accuracy and cost savings that is possible by adopting the use of automation testing.",
                      "Cucumber BDD": "Cucumber (BDD) simplifies the requirement capturing process. Requirements can be captured, broken down and simplified effortlessly; making the captured requirements readable to anyone within the organisation and in turn providing the required details and backbone to develop accurate test cases also known as ‘Feature Files’.",
                      "Automation Testing": "Automation testing has been steadily grown in popularity these past few years thanks to the time/ cost savings and efficiency that it offers. Companies throughout the world have or plan to use automation testing to rapidly speed up their test capabilities. Automation test engineers are in great demand and offer an average salary of £45,000+ (2018). Now is a great time to learn about automation test engineering and this course has been carefully developed to slowly introduce you from the basics, all the way to building advanced frameworks.",
                      "Keep Clicking! - Text will Appear After 5 Seconds!": "This text has appeared after 5 seconds!"}

        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.text_to_be_present_in_element(accordionTextAffectsPage.loadingButton, "LOADING COMPLETE."))

        # create list of titles
        blockTitlesText = accordionTextAffectsPage.getBlockTitlesText()

        # create list of texts
        blockDescriptions = accordionTextAffectsPage.getBlockDescriptionText()

        # create dict title: text
        blockRealText = {}
        for i in range(len(blockTitlesText)):
            blockRealText[blockTitlesText[i]] = blockDescriptions[i]

        for key in blockTestData.keys():
            assert blockRealText[key] == blockTestData[key]
