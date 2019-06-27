from seleniumbase import BaseCase
import os
import csv
from time import sleep
from selenium.common.exceptions import TimeoutException,NoSuchElementException,WebDriverException

class BaiDuWangPan(BaseCase):
    def test_Save(self):
        url = "https://pan.baidu.com/s/1qcGZRpmfkm0khzb0aREIlQ"
        h = self.driver.current_window_handle
        self.open(url)
        self.update_text("#nmm1R98","088n")
        sleep(5)
        h3 = self.driver.current_window_handle
        self.click("//*[@id='hifEl9j']/a/span/span")
        sleep(5)
        self.click("#layoutMain > div.frame-content > div.module-share-header > div > div.slide-show-right > div > div > div.x-button-box > a.g-button.g-button-blue > span > span")
        sleep(10)
        h2 = self.driver.window_handles
        print(h)
        print(h3)
        print(h2)

        sleep(5)