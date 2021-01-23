from selenium.webdriver.common.by import By

from utils.BasePage import BasePage
from utils.BaseElement import BaseElement


class CalculatorPage(BasePage):
    @property
    def legend(self):
        locator = (By.CSS_SELECTOR, 'legend')
        return BaseElement(self.driver, locator)

