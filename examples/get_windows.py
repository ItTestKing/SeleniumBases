from seleniumbase import BaseCase
from selenium.common.exceptions import NoSuchWindowException,TimeoutException,NoSuchElementException
from time import sleep

class MyTestDemo(BaseCase):
    def test_windos(self):
        self.open("http://www.baidu.com")
        sleep(5)
        h = self.driver.current_window_handle
        print(h)


"""
        try:
            self.open("http://www.baidu.com")
        except:TimeoutException
        try:
            title= self.driver.title
            if title == u"百度一下,你就知道":
                print(title)
            else:
                print("这不是百度首页")
        except:
            print("没有获取成功")
"""

