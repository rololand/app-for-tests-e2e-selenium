from utils.BaseElement import BaseElement
from selenium.webdriver.support.select import Select as SelectObj


class Select(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver=driver, locator=locator)
        self.select_obj = SelectObj(self.web_element)

    def select_by_text(self, text):
        self.select_obj.select_by_visible_text(text)
        return None

    @property
    def selected_text(self):
        return self.select_obj.first_selected_option.text

    @property
    def selected_value(self):
        return self.select_obj.first_selected_option.get_attribute('value')
