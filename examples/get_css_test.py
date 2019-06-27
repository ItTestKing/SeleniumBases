from seleniumbase import BaseCase
from time import sleep
from selenium.common.exceptions import TimeoutException,NoSuchElementException,ElementClickInterceptedException

class MyTest(BaseCase):
    def test_baidu(self):
        try:
            self.open("https://www.tiebazhushou.com")
     #   print( self.driver.get_cookies())
        except TimeoutException:
            print("time out")
#        sleep(2)
#        self.click('#sex > option:nth-child(2)')
        try:
            self.click('select[id= "province"] >option[value="31"]')
   #     self.click('option[value="31"]')
            self.click('select[id="city"] > option[value = "3101"]')
            self.click('select[id="county"] >option[value="310113"]')
            self.click('select[id="year"] > option:nth-child(1)')
            self.click('select[id = "sex"] > option:nth-child(2)')
            self.click('input[type = "button"][value = "生成"]')
        except NoSuchElementException:
            print("no such elements")
        try:
            result = self.get_text('body > div > div:nth-child(4) > table > tbody > tr:nth-child(1) > td:nth-child(3)')
            print("身份证号："+result)
        except NoSuchElementException:
            print("no such elements")

        sleep(10)

