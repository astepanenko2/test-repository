# coding: utf-8

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome("c:\\Users\\1\\selenium\\chromedriver.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_menu(driver):
    driver.get("http://localhost/litecart/en/")
    #driver.find_element_by_name("username").send_keys("admin")
    #driver.find_element_by_name("password").send_keys("admin")
    #driver.find_element_by_name("login").click()
    WebDriverWait(driver, 2).until(EC.title_is(u"Online Store | My Store"))

    products = driver.find_elements_by_class_name('product')
    assert len(products) > 0
    for product in products:
        assert len(product.find_elements_by_class_name('sticker')) == 1
    

