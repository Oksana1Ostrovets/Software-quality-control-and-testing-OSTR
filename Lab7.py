from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 

try:
    # 1. Тест: Відкриття сторінки Google Meet
    driver.get("https://meet.google.com/")

    # 2. Знаходимо елемент для введення коду
    code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form.meeting input.input"))
    )
    
    # 3. Вводимо тестовий код
    code_input.send_keys("vrx-chpi-zxw")

    # 4. Знаходимо та натискаємо кнопку "Приєднатись"
    join_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "form.meeting button.join-meeting"))
    )
    join_button.click()

    
finally:
    driver.quit()
