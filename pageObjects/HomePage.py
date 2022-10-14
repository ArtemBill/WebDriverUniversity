from selenium.webdriver.common.by import By

from pageObjects.AccordionTextAffects import AccordionTextAffects
from pageObjects.Actions import Actions
from pageObjects.AjaxLoader import AjaxLoader
from pageObjects.Autocomplete import Autocomplete
from pageObjects.ButtonClicks import ButtonClicks
from pageObjects.ContactUs import ContactUs, ContactUsExcel
from pageObjects.DatePicker import DatePicker
from pageObjects.DropdownMenu import DropdownMenu
from pageObjects.FileUpload import FileUpload
from pageObjects.HiddenElements import HiddenElements
from pageObjects.Iframe import Iframe
from pageObjects.LoginPortal import LoginPortal
from pageObjects.PopupAlerts import PopupAlerts
from pageObjects.Scrolling import Scrolling
from pageObjects.ToDoList import ToDoList


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    header = (By.CSS_SELECTOR, "#udemy-promo-thumbnail h1")
    contactUsPage = (By.ID, "contact-us")
    loginPortalPage = (By.ID, "login-portal")
    buttonClicksPage = (By.ID, "button-clicks")
    toDoListPage = (By.CSS_SELECTOR, "#to-do-list")
    pageObjectModelPage = (By.CSS_SELECTOR, "#page-object-model")
    accordionTextAffectsPage = (By.XPATH, "(//a[@id='page-object-model'])[2]")
    dropdownMenuPage = (By.ID, "dropdown-checkboxes-radiobuttons")
    ajaxLoaderPage = (By.CSS_SELECTOR, "#ajax-loader")
    actionsPage = (By.CSS_SELECTOR, "#actions")
    scrollingPage = (By.CSS_SELECTOR, "#scrolling-around")
    popupAlertsPage = (By.CSS_SELECTOR, "#popup-alerts")
    iframePage = (By.CSS_SELECTOR, "#iframe")
    hiddenElementsPage = (By.CSS_SELECTOR, "#hidden-elements")
    autocompletePage = (By.CSS_SELECTOR, "#autocomplete-textfield")
    fileUploadPage = (By.CSS_SELECTOR, "#file-upload")
    datePickerPage = (By.ID, "datepicker")


    def GetHeaderText(self):
        return self.driver.find_element(*HomePage.header)

    def openContactUsPage(self):
        self.driver.find_element(*HomePage.contactUsPage).click()
        contactUs = ContactUs(self.driver)
        contact_us_window = self.driver.window_handles[1]
        self.driver.switch_to.window(contact_us_window)
        return contactUs

    def openContactUsExcelPage(self):
        contactUsExcel = ContactUsExcel(self.driver)
        return contactUsExcel

    def openLoginPortalPage(self):
        self.driver.find_element(*HomePage.loginPortalPage).click()
        loginPortal = LoginPortal(self.driver)
        login_portal_window = self.driver.window_handles[1]
        self.driver.switch_to.window(login_portal_window)
        return loginPortal

    def openButtonClicksPage(self):
        self.driver.find_element(*HomePage.buttonClicksPage).click()
        buttonClicks = ButtonClicks(self.driver)
        button_clicks_window = self.driver.window_handles[1]
        self.driver.switch_to.window(button_clicks_window)
        return buttonClicks

    def openToDoListPage(self):
        self.driver.find_element(*HomePage.toDoListPage).click()
        toDoList = ToDoList(self.driver)
        to_do_list_window = self.driver.window_handles[1]
        self.driver.switch_to.window(to_do_list_window)
        return toDoList

    def openPageObjectModelPage(self):
        self.driver.find_element(*HomePage.pageObjectModelPage).click()
        pageObjectModel = Iframe(self.driver)
        page_Object_Model_window = self.driver.window_handles[1]
        self.driver.switch_to.window(page_Object_Model_window)
        return pageObjectModel

    def openAccordionTextAffectsPage(self):
        self.driver.find_element(*HomePage.accordionTextAffectsPage).click()
        accordionTextAffects = AccordionTextAffects(self.driver)
        accordion_and_text_affects_window = self.driver.window_handles[1]
        self.driver.switch_to.window(accordion_and_text_affects_window)
        return accordionTextAffects

    def openDropdownMenuPage(self):
        self.driver.find_element(*HomePage.dropdownMenuPage).click()
        dropdownMenu = DropdownMenu(self.driver)
        dropdownMenu_window = self.driver.window_handles[1]
        self.driver.switch_to.window(dropdownMenu_window)
        return dropdownMenu

    def openAjaxLoaderPage(self):
        self.driver.find_element(*HomePage.ajaxLoaderPage).click()
        ajaxLoader = AjaxLoader(self.driver)
        ajax_loader_window = self.driver.window_handles[1]
        self.driver.switch_to.window(ajax_loader_window)
        return ajaxLoader

    def openActionsPage(self):
        self.driver.find_element(*HomePage.actionsPage).click()
        actions = Actions(self.driver)
        actions_window = self.driver.window_handles[1]
        self.driver.switch_to.window(actions_window)
        return actions

    def openScrollingPage(self):
        self.driver.find_element(*HomePage.scrollingPage).click()
        scrolling = Scrolling(self.driver)
        scrolling_window = self.driver.window_handles[1]
        self.driver.switch_to.window(scrolling_window)
        return scrolling

    def openPopupAlertsPage(self):
        self.driver.find_element(*HomePage.popupAlertsPage).click()
        popupAlerts = PopupAlerts(self.driver)
        popup_alerts_window = self.driver.window_handles[1]
        self.driver.switch_to.window(popup_alerts_window)
        return popupAlerts

    def openIframePage(self):
        self.driver.find_element(*HomePage.iframePage).click()
        iframe = Iframe(self.driver)
        iframe_window = self.driver.window_handles[1]
        self.driver.switch_to.window(iframe_window)
        self.driver.switch_to.frame("frame")
        return iframe

    def openHiddenElementsPage(self):
        self.driver.find_element(*HomePage.hiddenElementsPage).click()
        hiddenElements = HiddenElements(self.driver)
        hiddenElements_window = self.driver.window_handles[1]
        self.driver.switch_to.window(hiddenElements_window)
        return hiddenElements

    def openAutocompletePage(self):
        self.driver.find_element(*HomePage.autocompletePage).click()
        autocomplete = Autocomplete(self.driver)
        autocomplete_window = self.driver.window_handles[1]
        self.driver.switch_to.window(autocomplete_window)
        return autocomplete

    def openFileUploadPage(self):
        self.driver.find_element(*HomePage.fileUploadPage).click()
        fileUpload = FileUpload(self.driver)
        file_upload_window = self.driver.window_handles[1]
        self.driver.switch_to.window(file_upload_window)
        return fileUpload

    def openDatePickerPage(self):
        self.driver.find_element(*HomePage.datePickerPage).click()
        datePicker = DatePicker(self.driver)
        datepicker_window = self.driver.window_handles[1]
        self.driver.switch_to.window(datepicker_window)
        return datePicker




















