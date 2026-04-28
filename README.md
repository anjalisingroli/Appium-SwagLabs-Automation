# Appium SwagLabs Automation Framework

This project is a mobile automation testing framework built using **Appium, Python, and Pytest**.  
It automates the checkout functionality of the Swag Labs mobile application.

## Technologies Used

- Python
- Appium
- Pytest
- Page Object Model (POM)
- Pytest HTML Report

## Project Structure

Swaglabs
│
├── pages
│    ├── login_page.py
│    ├── product_page.py
│    └── cart_page.py
│
├── tests
│    └── test_checkout.py
│
├── utils
│    └── driver_setup.py
│
├── conftest.py
│
└── report.html


## Test Scenario

The automated test performs the following steps:

1. Launch the mobile application
2. Login with valid credentials
3. Add a product to the cart
4. Open the cart
5. Proceed to checkout
6. Fill user details
7. Scroll and click the Finish button

## How to Run the Tests

1. Install dependencies

pip install -r requirements.txt

2. Start Appium server

appium

3. Run tests

pytest -v --html=report.html

## Framework Design

This framework follows the **Page Object Model (POM)** design pattern where:

- Each screen is represented by a separate page class
- Test cases call methods from page classes
- Driver setup is handled using pytest fixtures

## Author

Anjali Singroli
