from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):

        wait = WebDriverWait(self.driver,10)

        add_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.TextView[@text="ADD TO CART"]'))
        )

        add_btn.click()

    def open_cart(self):

        self.driver.find_element("accessibility id","test-Cart").click()