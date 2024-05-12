from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ініціалізація веб-драйвера
driver = webdriver.Chrome()

# Відкриття сторінки входу
driver.get("https://www.speakua.com/my-account/")

# Знаходимо поля введення користувача та пароля
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

# Введення даних користувача та пароля
username_input.clear()
username_input.send_keys("ostrovets.oksana@chnu.edu.ua")
password_input.clear()
password_input.send_keys("Надійнийпароль111")

# Знаходимо кнопку входу
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "login")))
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loader-section")))

# Клацання на кнопку входу
login_button.click()

# Очікування переходу на нову сторінку
WebDriverWait(driver, 10).until(EC.url_contains("my-account"))

# Перевірка результату тесту
if "my-account" in driver.current_url:
    print("Успішний вхід. Користувач увійшов до свого облікового запису.")
else:
    print("Помилка. Користувач не ввійшов до свого облікового запису.")

# Закриття веб-драйвера
driver.quit()
