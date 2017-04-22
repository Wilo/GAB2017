from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class postTestCase(TestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(postTestCase, self).setUp()

    def tearDown(self):
        self.selenium.maximize_window()
        self.selenium.get("http://localhost:8000/blog/")
        self.selenium.quit()
        super(postTestCase, self).tearDown()
