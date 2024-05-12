import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_speakua_website():
    print("Starting test...")
    
    # Запускаємо браузер Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    
    print("Browser launched.")
    
    # Відкриваємо веб-сайт speakua.com
    driver.get("https://www.speakua.com/")
    print("Website opened.")
    
    # Додамо затримку перед перевіркою заголовка
    sleep(3)
    
    # Перевіряємо, чи фактичний заголовок містить певне ключове слово
    expected_keyword = "Speak Ukrainian"
    assert expected_keyword in driver.title
    
    print("Title verified.")
    
    # Закриваємо браузер
    driver.quit()
    print("Browser closed.")

test_speakua_website()
