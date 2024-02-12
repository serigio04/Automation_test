import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.driver = webdriver.Chrome("C:/Users/jenif/Desktop/azulschool/python/tests/chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_example():
        print("Test")
        assert True
    
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()