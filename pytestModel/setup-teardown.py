import time

import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# def test_demokk():
#     print("    这里是一个函数", 250*800)

class TestPractice():
    def setup_method(self):
        print("方法前")

    def teardown_method(self):
        print("方法后")

    def setup_class(self):
        print("类前")
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_class(self):
        print("类后")

    def test_demo(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.set_window_size(1296, 696)
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        self.vars["window_handles"] = self.driver.window_handles
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Selenium automates browsers. That\'s it!").click()


def setup_function():
    print("函数前")

def teardown_function():
    print("函数后")

def setup_module():
    print("模块前")

def teardown_module():
    print("模块后")

if __name__ == "__main__":
    pytest.main()