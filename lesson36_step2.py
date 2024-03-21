from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

def test_guest_could_press_button_enter(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#ember408").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("semashko@fgoupsk.ru")
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("semashko@fgoupsk.ru")
    browser.find_element(By.CSS_SELECTOR, ".button_with-loader").click()
    browser.find_element(By.CSS_SELECTOR, "#ember467")

