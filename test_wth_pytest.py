import pytest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestLink1():
    @pytest.mark.skip
    def test_reg1(self, browser) :
        browser.get(link1)
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        last_name.send_keys("Smirnov")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("Ivan@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elem = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elem.text
        assert welcome_text == "Congratulations! You have successfully registered!", "No welcome_text"

    @pytest.mark.smoke
    def test_reg2(self, browser) :
        browser.get(link1)
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        last_name.send_keys("Smirnov")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("Ivan@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elem = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elem.text
        assert welcome_text == "Congratulations! You  successfully registered!", "No welcome_text"
class TestLink2():
    @pytest.mark.xfail
    def test_reg3(self, browser) :
        browser.get(link2)
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        last_name.send_keys("Smirnov")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("Ivan@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elem = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elem.text
        assert welcome_text == "Congratulations! You have successfully registered!", "No welcome_text"
if __name__ == '__main__':
    pytest.main()
