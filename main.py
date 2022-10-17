from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get(link1)
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        last_name.send_keys("Smirnov")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("Ivan@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elem.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()
    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get(link2)
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        last_name.send_keys("Smirnov")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("Ivan@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elem.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()
if __name__ == '__main__':
    unittest.main(warnings='ignore')