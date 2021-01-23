from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement(object):
    def __init__(self, driver, locator,):
        self.driver = driver
        self.locator = locator
        self.web_element = self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10)\
            .until(ec.visibility_of_element_located(locator=self.locator))
        return element

    @property
    def text(self):
        return self.web_element.text
