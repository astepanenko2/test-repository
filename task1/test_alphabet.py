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
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"My Store"))
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    WebDriverWait(driver, 10).until(EC.title_is(u"Countries | My Store"))

    list = driver.find_element_by_css_selector("[name=countries_form]")
    countries = list.find_elements_by_class_name('row')
    country_names = []
    for country_row in countries:
        name = country_row.find_elements_by_tag_name('td')[4].get_attribute("textContent")
        country_names.append(name)
    sorted_list = sorted(country_names)
    assert country_names == sorted_list
    # for i in range(len(countries)):
    #     assert countries[i] == sorted_list[i]

