from selenium.webdriver.common.by import By


class AccordionTextAffects:
    def __init__(self, driver):
        self.driver = driver

    blockTitles = (By.XPATH, "(//div[@class='col-lg-12'])[1]/button")

    # first 3 texts
    blockDescriptions = (By.XPATH, "//div[@class='panel']/p")
    # hidden text
    hiddenDescription = (By.XPATH, "//div[@id='timeout']")

    loadingButton = (By.CSS_SELECTOR, "#hidden-text")

    def getBlockTitlesText(self):
        blockTitles = self.driver.find_elements(*AccordionTextAffects.blockTitles)
        blockTitlesText = []
        for blockTitle in blockTitles:
            blockTitlesText.append(blockTitle.text)
        return blockTitlesText

    def getBlockDescriptionText(self):
        blockDescriptions = self.driver.find_elements(*AccordionTextAffects.blockDescriptions)
        # add hidden text
        blockDescriptions.append(self.driver.find_element(*AccordionTextAffects.hiddenDescription))
        blockDescriptionsText = []
        for elem in blockDescriptions:
            blockDescriptionsText.append(elem.text)
        return blockDescriptionsText



