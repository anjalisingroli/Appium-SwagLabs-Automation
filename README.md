# Appium SwagLabs Automation Framework

This project is a **Mobile Automation Testing Framework** built using **Python, Appium, and Pytest**.  
The framework automates the checkout functionality of the Swag Labs mobile application.

---

## Technologies Used

- Python
- Appium
- Pytest
- Selenium WebDriver
- Pytest HTML Report

---

## Framework Design

The framework follows the **Page Object Model (POM)** design pattern.

Benefits of POM:

- Clean code structure
- Reusable methods
- Easy maintenance
- Scalable automation framework

---

## Framework Architecture

Test Layer  
│  
▼  
tests/test_checkout.py  
│  
▼  
Page Layer (Page Object Model)  
│  
├── LoginPage  
├── ProductPage  
└── CartPage  
│  
▼  
Driver Setup  
│  
conftest.py (Pytest Fixture)  
│  
▼  
Appium Driver  
│  
▼  
Mobile Application  

---

## Project Structure

```
Swaglabs
│
├── pages
│   ├── login_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── tests
│   └── test_checkout.py
│
├── utils
│
├── assets
│
├── conftest.py
├── requirements.txt
└── report.html
```

---

## Test Scenario

The automated test performs the following steps:

1. Launch the mobile application
2. Login with valid credentials
3. Add a product to the cart
4. Open the cart
5. Click checkout
6. Fill user information
7. Scroll and click the Finish button

---

## How to Run the Tests

### Install dependencies

```
pip install -r requirements.txt
```

### Start Appium Server

```
appium
```

### Run the Tests

```
pytest -v --html=report.html
```

---

## Test Report

After test execution, an HTML report is generated using pytest-html.

---

## Author

Anjali Singroli
