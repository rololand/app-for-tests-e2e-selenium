from selenium.webdriver.common.by import By

from utils.BaseElement import BaseElement
from utils.BasePage import BasePage
from .Calculator import Calculator


class App(BasePage, Calculator):
    @property
    def calculator_menu_button(self):
        locator = (By.ID, 'menuButtonCalculator')
        return BaseElement(self.driver, locator)

    @property
    def to_do_list_menu_button(self):
        locator = (By.ID, 'menuButtonTaskList')
        return BaseElement(self.driver, locator)
