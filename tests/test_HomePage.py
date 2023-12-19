import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass




class TestHomePage(BaseClass):


    def test_formSubmission(self, getData):

        homepage = HomePage(self.driver)
        log = self.getLogger()
        log.info("First name is" +getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params = HomePageData.getTestData())
    def getData(self, request):
        return request.param