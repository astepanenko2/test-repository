# coding: utf-8

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    wd = webdriver.Chrome("c:\\Users\\1\\selenium\\chromedriver.exe", desired_capabilities=d)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_menu(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"Catalog | My Store"))

    duck_list = driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr[contains(@class, 'row')]")

    idx = 3
    while idx < len(duck_list):
        duck_list = driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr[contains(@class, 'row')]")
        duck = duck_list[idx]
        duck.find_element_by_xpath("td[3]//a").click()

        log_browser = driver.get_log("browser")
        print(log_browser)

        assert len(log_browser) == 0
        driver.back()
        idx +=1
