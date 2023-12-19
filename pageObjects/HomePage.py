from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    lastName = (By.NAME, "email")
    exampleCheck = (By.ID, "exampleCheck1")
    form = (By.ID, "exampleFormControlSelect1")
    button = (By.XPATH, "//input[@value='Submit']")
    alert = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getLastName(self):
        return self.driver.find_element(*HomePage.lastName)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.exampleCheck)

    def getGender(self):
        return self.driver.find_element(*HomePage.form)

    def submitForm(self):
        return self.driver.find_element(*HomePage.button)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.alert)