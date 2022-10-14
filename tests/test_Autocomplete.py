import time
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_Autocomplete(BaseClass):

    # Check autocomplete
    def test_Autocomplete(self):
        homePage = HomePage(self.driver)
        autocompletePage = homePage.openAutocompletePage()

        # Choose word from dropdown and check text in input
        autocompletePage.enterText("A")
        time.sleep(0.5)
        products = autocompletePage.getProductList()
        for product in products:
            if product.text == "Apple":
                product.click()
                break
        assert autocompletePage.getEnteredText() == "Apple"

        autocompletePage.Submit()

        autocompletePage.enterText("P")
        time.sleep(0.5)
        products = autocompletePage.getProductList()
        for product in products:
            if product.text == "Pizza":
                product.click()
                break
        assert autocompletePage.getEnteredText() == "Pizza"

