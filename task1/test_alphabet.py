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
    idx = 0
    while idx < len(countries):
        list = driver.find_element_by_css_selector("[name=countries_form]")
        countries = list.find_elements_by_class_name('row')
        country_row = countries[idx]
        name = country_row.find_elements_by_tag_name('td')[4].get_attribute("textContent")
        country_names.append(name)
        zones = int(country_row.find_elements_by_tag_name('td')[5].get_attribute("textContent"))
        if zones > 0:
            country_row.find_elements_by_tag_name('td')[4].find_element_by_tag_name("a").click()
            time.sleep(2)
            child_country_names = []
            child_list = driver.find_element_by_id("table-zones").find_elements_by_tag_name("tr")

            for child_row in child_list[1:-1]:
                child_name = child_row.find_elements_by_tag_name('td')[2].get_attribute("textContent")
                child_country_names.append(child_name)
            sorted_child_list = sorted(child_country_names)
            assert child_country_names == sorted_child_list
            driver.back()
        idx += 1
    sorted_list = sorted(country_names)
    assert country_names == sorted_list


