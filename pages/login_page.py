import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self):

        time.sleep(3)

        self.driver.find_element("accessibility id","test-Username").send_keys("standard_user")
        self.driver.find_element("accessibility id","test-Password").send_keys("secret_sauce")
        self.driver.find_element("accessibility id","test-LOGIN").click()

        time.sleep(5)