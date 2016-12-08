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
    driver.get("http://localhost/litecart/en/create_account")
    WebDriverWait(driver, 10).until(EC.title_is(u"Create Account | My Store"))

    driver.find_element_by_name("firstname").send_keys("alona")
    driver.find_element_by_name("lastname").send_keys("step")
    driver.find_element_by_name("address1").send_keys("shulyavka")
    driver.find_element_by_name("postcode").send_keys("04112")
    driver.find_element_by_name("city").send_keys("Kyiv")
    driver.find_element_by_name("email").send_keys("for21page@gm.com")
    driver.find_element_by_name("phone").send_keys("+380501234567")
    driver.find_element_by_name("password").send_keys("12345678")
    driver.find_element_by_name("confirmed_password").send_keys("12345678")
    driver.find_element_by_name("create_account").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"Online Store | My Store"))

    driver.find_element_by_css_selector("td.account").find_element_by_tag_name("nav").find_element_by_css_selector("ul.list-vertical").find_elements_by_tag_name("li")[4].find_element_by_tag_name("a").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"Online Store | My Store"))

    driver.find_element_by_css_selector("td.account").find_element_by_tag_name("nav").find_element_by_css_selector("ul.list-vertical").find_elements_by_tag_name("li")[3].find_element_by_tag_name("a").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"Login | My Store"))
    driver.find_element_by_name("email").send_keys("for21page@gm.com")
    driver.find_element_by_name("password").send_keys("12345678")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"Online Store | My Store"))



