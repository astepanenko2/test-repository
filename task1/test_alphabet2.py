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
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    WebDriverWait(driver, 10).until(EC.title_is(u"Geo Zones | My Store"))

    table = driver.find_element_by_class_name("dataTable")
    countries = table.find_elements_by_css_selector("tr")
    idx = 1
    while idx < len(countries)-1:
        table = driver.find_element_by_class_name("dataTable")
        countries = table.find_elements_by_css_selector("tr")
        country = countries[idx]
        country.find_elements_by_tag_name('td')[2].find_element_by_tag_name("a").click()

        zones_list = []
        zones = driver.find_element_by_id("table-zones").find_elements_by_tag_name("tr")
        for zone in zones[1:-1]:
            zone_name = zone.find_elements_by_tag_name("td")[2].find_element_by_tag_name(
                "select"
            ).find_element_by_css_selector(
                "option[selected=selected]"
            ).get_attribute("textContent")
            zones_list.append(zone_name)
        sorted_zones_list = sorted(zones_list)
        assert sorted_zones_list == zones_list
        idx +=1
        driver.back()


