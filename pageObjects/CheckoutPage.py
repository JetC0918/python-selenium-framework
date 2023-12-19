from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cartTitle = (By.XPATH, "//div[@class='card h-100']" )
    cartFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    successButton =(By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCartTitle(self):
        return self.driver.find_elements(*CheckOutPage.cartTitle)

    def getCartFooter(self):
        return self.driver.find_elements(*CheckOutPage.cartFooter)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.checkoutButton)

    def getSuccessButton(self):
        self.driver.find_element(*CheckOutPage.successButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage