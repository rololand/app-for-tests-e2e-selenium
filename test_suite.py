from selenium import webdriver
from calculator.CalculatorPage import CalculatorPage

driver = webdriver.Chrome()
url_calculator = 'https://rololand.github.io/app-for-tests'
calculator = CalculatorPage(driver=driver, url=url_calculator)


def setup_function():
    calculator.go()


def teardown_function():
    calculator.quit()


def test_check_legend_name():
    assert calculator.legend.text == 'Kalkulator:'
