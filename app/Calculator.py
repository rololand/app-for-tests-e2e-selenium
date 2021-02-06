from selenium.webdriver.common.by import By

from utils.BasePage import BasePage
from utils.BaseElement import BaseElement
from utils.Input import Input
from utils.Select import Select


class Calculator(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def legend(self):
        locator = (By.CSS_SELECTOR, 'legend')
        return BaseElement(self.driver, locator)

    @property
    def x_input(self):
        locator = (By.ID, 'x_value')
        return Input(self.driver, locator)

    @property
    def y_input(self):
        locator = (By.ID, 'y_value')
        return Input(self.driver, locator)

    @property
    def result(self):
        locator = (By.ID, 'result')
        return Input(self.driver, locator)

    @property
    def operations(self):
        locator = (By.ID, 'operation')
        return Select(self.driver, locator)

    @property
    def x_label(self):
        locator = (By.XPATH, '//label[@for="x_value"]')
        return BaseElement(self.driver, locator)

    @property
    def y_label(self):
        locator = (By.XPATH, '//label[@for="y_value"]')
        return BaseElement(self.driver, locator)

    @property
    def operation_label(self):
        locator = (By.XPATH, '//label[@for="operation"]')
        return BaseElement(self.driver, locator)

    @property
    def result_label(self):
        locator = (By.XPATH, '//label[@for="result"]')
        return BaseElement(self.driver, locator)
