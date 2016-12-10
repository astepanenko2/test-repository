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
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"Catalog | My Store"))

    driver.find_element_by_xpath("(//div//a[contains(@class, 'button')])[2]").click()
    WebDriverWait(driver, 10).until(EC.title_is(u"Add New Product | My Store"))

    # Tab General
    driver.find_element_by_xpath(".//*[contains(text(), ' Enabled')]").click()
    new_duck = "black duck"
    driver.find_element_by_name("name[en]").send_keys(new_duck)
    driver.find_element_by_name("code").send_keys("rd011")
    driver.find_element_by_xpath(".//*[contains(text(), 'Rubber Ducks')]").click()

    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys("13")

    driver.find_element_by_xpath("//select[@name='sold_out_status_id']/option[text()='Temporary sold out']").click()
    driver.find_element_by_name("new_images[]").send_keys("C:\\Users\\1\\Desktop\\21eD5+lZlbL.jpg")

    # Tab Information
    driver.find_element_by_xpath("//ul[contains (@class, 'index')]//li[2]//a").click()
    driver.find_element_by_xpath("//select[@name='manufacturer_id']/option[text()='ACME Corp.']").click()
    driver.find_element_by_name("short_description[en]").send_keys("new black duck")
    driver.find_element_by_class_name("trumbowyg-editor").send_keys("brand new black duck")

    # Tab Prices
    driver.find_element_by_xpath("//ul[contains (@class, 'index')]//li[4]//a").click()
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("13")
    driver.find_element_by_name("prices[USD]").send_keys("20")
    driver.find_element_by_name("save").click()

    product_list = []
    name_list = driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tbody//tr[contains(@class, 'row')]")
    for name_row in name_list:
        text = name_row.find_elements_by_tag_name('td')[2].find_element_by_tag_name("a").get_attribute("textContent")
        product_list.append(text)
    assert new_duck in product_list

    # delete new item
    driver.find_element_by_xpath(".//*[contains(text(), '{}')]/../../td[1]".format(new_duck)).click()
    driver.find_element_by_name("delete").click()
    driver.switch_to.alert.accept()
    time.sleep(1)



