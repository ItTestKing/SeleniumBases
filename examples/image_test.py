"""
Pull an image from a website and save it as a PNG file.
"""

from seleniumbase import BaseCase


class ImageTest(BaseCase):

    def test_pull_image_from_website(self):
        self.open("https://xkcd.com/1117/")
        selector = "#comic"
        file_name = "comicmap.png"
        folder = "images_exported"
        self.save_element_as_image_file(selector, file_name, folder)
        print('"%s/%s" has been saved!' % (folder, file_name))
    def test_baidu(self):
        self.open("https://www.baidu.com")
        selector = "#lg"
        file_name = "baidu.png"
        folder = "images_exported"
        self.save_element_as_image_file(selector,file_name,folder)
    def test_baidu1(self):
        self.open("https://www.baidu.com")
        selector = "[name='wd']"
        file_name = "baidu1.png"
        folder = "images_exported"
        self.save_element_as_image_file(selector,file_name,folder)
