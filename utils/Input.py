from utils.BaseElement import BaseElement


class Input(BaseElement):
    def send_keys(self, keys_to_send):
        self.web_element.clear()
        self.web_element.send_keys(keys_to_send)
        return None

    @property
    def value(self):
        return self.web_element.get_attribute('value')
