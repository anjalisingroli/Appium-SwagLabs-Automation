from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver


    def checkout(self):

        wait = WebDriverWait(self.driver,10)

        checkout_btn = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"test-CHECKOUT"))
        )

        checkout_btn.click()


    def fill_details(self):

        wait = WebDriverWait(self.driver,10)

        first_name = wait.until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,"test-First Name"))
        )

        first_name.send_keys("Anjali")

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"test-Last Name").send_keys("Singroli")

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"test-Zip/Postal Code").send_keys("1234")

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"test-CONTINUE").click()


    def finish_order(self):

        self.driver.find_element(
            "-android uiautomator",
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("FINISH"))'
        ).click()