from pytest import fixture
from selenium import webdriver
from calculator.CalculatorPage import CalculatorPage

@fixture(scope='class')
def calculator():
    driver = webdriver.Chrome()
    url_calculator = 'https://rololand.github.io/app-for-tests'
    calculator = CalculatorPage(driver=driver, url=url_calculator)
    calculator.go()
    yield calculator
    calculator.quit()