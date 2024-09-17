import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome('C:\Users\007ve\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\chromedriver.exe')

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.navegador.get('https://brpioneer.accenture.com/originacao-auto/login/sign-in')

    def test_find_username_field(self):
        username_field = self.navegador.find_element(By.XPATH, '//*[@id="mat-input-0"]')
        self.assertIsNotNone(username_field)

    def test_find_password_field(self):
        password_field = self.navegador.find_element(By.XPATH, '//*[@id="mat-input-1"]')
        self.assertIsNotNone(password_field)

    @classmethod
    def tearDownClass(cls):
        cls.navegador.quit()

if __name__ == "__main__":
    unittest.main()