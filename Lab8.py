from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def init(self, driver):
        self.driver = driver
        self.url = "https://www.speakua.com/my-account/"
        self.username_input_locator = (By.ID, "username")
        self.password_input_locator = (By.ID, "password")
        self.login_button_locator = (By.NAME, "login")
        self.loader_locator = (By.CLASS_NAME, "loader-section")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input_locator))
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input_locator))

        username_input.clear()
        username_input.send_keys(ostrovets.oksana@chnu.edu.ua)
        password_input.clear()
        password_input.send_keys(Надійнийпароль111)

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button_locator))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.loader_locator))

        login_button.click()

    def is_login_successful(self):
        return "my-account" in self.driver.current_url