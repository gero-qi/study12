from selenium import webdriver
from common.framelog import Framelog


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.log = Framelog().log()

    def findele(self, *args):
        try:
            return self.driver.find_element(*args)
        except:
            self.log.erro('未找到该元素')

    def js(self, str):
        self.driver.ex111

    def test（）：
