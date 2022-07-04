# vitkac_selenium_tests

# General info:

Automation test project which includes 2 tests:

First one - in the *new_account_test* file
- registers new user with wrong e-mail, 
- fills out the registration form,
- checks content after an unsuccessful attempt.

Second one - in the *purchase_test* file
- checks the ability to adding products to the basket,
- checks the correct amount of products in the basket.

## Technologies
Project leverages Unittest framework and Selenium WebDriver in Python

## Setup

Before run this project, install: 
```
$ pip3 install Faker

$ pip3 install selenium

$ pip3 install webdriver_manager
```
