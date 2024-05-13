import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_menu_item_and_register_button_existence():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://www.speakua.com/")
    
    try:
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "primary-menu"))
        )
        
        home_menu_item = menu.find_element(By.XPATH, "//li[@class='active menu-item-2230 aligned-left']")
        
        assert home_menu_item is not None
        
        register_button = driver.find_element(By.XPATH, "//a[@class='register']")
        assert register_button is not None
        
    finally:
        driver.quit()

test_menu_item_and_register_button_existence()