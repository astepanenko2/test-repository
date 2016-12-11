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
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"Countries | My Store"))

    country_list = driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr[contains(@class, 'row')]")
                                 #"//td[7]//a").click()

    idx = 0
    while idx < len(country_list):
        country_list = driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr[contains(@class, 'row')]")
        country = country_list[idx]
        country.find_element_by_xpath("td[7]//a").click()
        WebDriverWait(driver, 5).until(EC.title_is(u"Edit Country | My Store"))

        main_handle = driver.current_window_handle
        driver.find_element_by_xpath("//td[@id='content']//form//tr[2]//td//a").click()

        WebDriverWait(driver, 5).until(lambda driver: len(driver.window_handles) > 1)

        all_handles = driver.window_handles
        if all_handles[0] == main_handle:
            new_handle = all_handles[1]
        else:
            new_handle = all_handles[0]

        driver.switch_to_window(new_handle)
        print(driver.find_element_by_xpath("//h1[contains(@class, 'firstHeading')]").get_attribute("textContent"))
        driver.close()
        driver.switch_to_window(main_handle)
        driver.back()
        idx +=1
    print(idx)




