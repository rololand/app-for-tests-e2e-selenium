from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10)\
            .until(ec.visibility_of_element_located(locator=self.locator))
        return element

    def click(self):
        element = WebDriverWait(self.driver, 10)\
            .until(ec.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def get_attribute(self, attribute):
        return self.web_element.get_attribute(attribute)

    def get_css_value(self, css_property):
        return self.web_element.value_of_css_property(css_property)

    @property
    def text(self):
        return self.web_element.text
