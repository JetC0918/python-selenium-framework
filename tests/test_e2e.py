import time

import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)
        # //a[contains(@href,'shop')] a[href*='shop']

        checkOutPage = homePage.shopItems()
        log.info("Getting all the product titles")
        carts = checkOutPage.getCartTitle()
        i = -1
        for cart in carts:
            i += 1
            productName = cart.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == 'Blackberry':
                checkOutPage.getCartFooter()[i].click()


        checkOutPage.getCheckoutButton().click()
        confirmPage = checkOutPage.getSuccessButton()

        log.info("Entering country name as an")
        confirmPage.getCountryInput().send_keys("an")

        self.verifyLinkPresence("France")

        confirmPage.getCheckboxInput().click()
        confirmPage.getSubmitButton().click()
        successText = confirmPage.getSuccessText().text
        log.info("Text received from application is" +successText)

        assert "Success" in successText