import pytest
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
txt = ""
@pytest.mark.parametrize('link', links)
class TestLogin:
    def test_guest_could_press_button_enter(self, browser, link):
        browser.get(f"https://stepik.org/lesson/{link}/step/1")
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember408")))
        button.click()
        login = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_login_email")))
        login.send_keys("dmitriy.semashko@gmail.com")
        password = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_login_password")))
        password.send_keys("Qwerty123")
        browser.find_element(By.CSS_SELECTOR, ".button_with-loader").click()

        answer = math.log(int(time.time() + 1.2))
        answer_txt = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ember-text-area")))
        answer_txt.send_keys(str(answer))
        answer_btn = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.submit-submission")))
        answer_btn.click()

        feedback = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
        assert feedback == "Correct!", "Ответ неверный"
        return feedback

    if __name__ == "__main__":
        feedback = test_guest_could_press_button_enter()
        txt = txt + feedback
        print(txt)


