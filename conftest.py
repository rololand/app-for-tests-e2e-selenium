from pytest import fixture
from selenium import webdriver
from app.App import App


@fixture(scope='class')
def app():
    driver = webdriver.Chrome()
    url_app = 'https://rololand.github.io/app-for-tests'
    app = App(driver=driver, url=url_app)
    app.go()
    yield app
    app.quit()
