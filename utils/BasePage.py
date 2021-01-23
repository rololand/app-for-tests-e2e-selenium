class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go(self):
        self.driver.get(self.url)
        return None

    def quit(self):
        self.driver.quit()
        return None
