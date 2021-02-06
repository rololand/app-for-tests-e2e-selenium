from selenium.webdriver.common.by import By

from utils.BaseElement import BaseElement
from utils.Input import Input
from utils.Select import Select


class TaskList(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def new_task_input(self):
        locator = (By.ID, 'newTask')
        return Input(self.driver, locator)

    @property
    def new_task_button(self):
        locator = (By.ID, 'addTaskButton')
        return BaseElement(self.driver, locator)

    @property
    def task_list(self):
        locator = (By.XPATH, '//div[@id="taskList"]/fieldset/ul')
        return BaseElement(self.driver, locator)

    def get_list_of_tasks(self):
        tasks = self.task_list.get_attribute("textContent")
        list_of_tasks = tasks.split('X')
        return list_of_tasks[:-1]

    def add_new_task(self, task_text):
        self.new_task_input.send_keys(task_text)
        self.new_task_button.click()

    def mark_as_done(self, task_text):
        xpath = '//div[@class="taskElement" and text()="'+task_text+'"]'
        locator = (By.XPATH, xpath)
        element = BaseElement(self.driver, locator)
        element.click()
        return None

    def is_mark_as_done(self, task_text):
        xpath = '//div[@class="taskElement taskDone" and text()="' + task_text + '"]'
        locator = (By.XPATH, xpath)
        element = BaseElement(self.driver, locator)
        property_value = element.get_css_value('text-decoration')
        return "line-through" in property_value


    def delete_task(self, task_text):
        xpath = '//div[@class="taskElement" and text()="' + task_text + '"]/../div[@class="deleteTaskButton"]'
        locator = (By.XPATH, xpath)
        element = BaseElement(self.driver, locator)
        element.click()
        return None

    def delete_done_task(self, task_text):
        xpath = '//div[@class="taskElement taskDone" and text()="' + task_text + '"]/../div[@class="deleteTaskButton"]'
        locator = (By.XPATH, xpath)
        element = BaseElement(self.driver, locator)
        element.click()
        return None



