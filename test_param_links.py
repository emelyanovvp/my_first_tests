import pytest
from selenium.webdriver.common.by import By
import time
import math

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
def test_correct_answer(browser, links):
    browser.get(links)
    browser.implicitly_wait(10)
    answer = str(math.log(int(time.time() - 2.9)))
    text_area = browser.find_element(By.CSS_SELECTOR, 'textarea')
    text_area.send_keys(answer)
    browser.find_element(By.CLASS_NAME,"submit-submission").click()
    welcome_text_elem = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    welcome_text = welcome_text_elem.text
    print(welcome_text)
    assert welcome_text == "Correct!"

if __name__ == '__main__':
    pytest.main()






