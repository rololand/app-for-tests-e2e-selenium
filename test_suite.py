import time
from selenium import webdriver

from calculator.CalculatorPage import CalculatorPage

driver = webdriver.Chrome()
url_calculator = 'https://rololand.github.io/app-for-tests'
calculator = CalculatorPage(driver=driver, url=url_calculator)

calculator.go()

time.sleep(3)
calculator.quit()
