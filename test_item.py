import time

import pytest
from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary")