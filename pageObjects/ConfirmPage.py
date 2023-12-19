from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryInput = (By.ID, "country")
    checkboxInput = (By.CSS_SELECTOR, ".checkbox-primary")
    submitButton = (By.CSS_SELECTOR, "input[type*='submit']")
    successText = (By.CSS_SELECTOR, ".alert-success")

    def getCountryInput(self):
        return self.driver.find_element(*ConfirmPage.countryInput)

    def getCheckboxInput(self):
        return self.driver.find_element(*ConfirmPage.checkboxInput)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText)