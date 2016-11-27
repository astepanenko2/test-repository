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

    menu_parent = driver.find_element_by_id('box-apps-menu')
    top_links = menu_parent.find_elements_by_id('app-')
    top_idx = 0
    while top_idx < len(top_links):
        top_links[top_idx].click()
        assert driver.find_element_by_tag_name('h1')
        menu_parent = driver.find_element_by_id('box-apps-menu')
        top_links = menu_parent.find_elements_by_id('app-')
        second_links = top_links[top_idx].find_elements_by_tag_name('li')
        if not second_links:
            top_idx += 1
            continue
        second_idx = 0
        while second_idx < len(second_links):
            second_links[second_idx].click()
            assert driver.find_element_by_tag_name('h1')
            second_idx += 1
            menu_parent = driver.find_element_by_id('box-apps-menu')
            top_links = menu_parent.find_elements_by_id('app-')
            second_links = top_links[top_idx].find_elements_by_tag_name('li')
        top_idx += 1