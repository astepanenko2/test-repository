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
    WebDriverWait(driver, 10).until(EC.title_is(u"Online Store | My Store"))

    current_count = 0
    product_list = driver.find_elements_by_xpath("//div[@id='box-latest-products']//li[contains(@class, 'product')]")
    assert len(product_list) > 0
    idx = 0
    while idx < len(product_list[:3]):
        product_list = driver.find_elements_by_xpath("//div[@id='box-latest-products']//li[contains(@class, 'product')]")
        product = product_list[idx]
        product.find_element_by_xpath("a[contains(@class, 'link')]").click()
        if driver.find_elements_by_name("options[Size]"):
            driver.find_element_by_xpath("//select[@name='options[Size]']/option[text()='Large +$5']").click()

        driver.find_element_by_name("add_cart_product").click()
        current_count += 1
        WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@id='cart']//a[@class='content']//span[@class='quantity']"),
                str(current_count)
            )
        )
        driver.find_element_by_xpath("//i[contains(@class, 'fa-home')]").click()
        idx += 1

    driver.find_element_by_xpath("//div[@id='cart']//a[@class='link']").click()
    for i in range(3):
        product_row = driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr")[1]
        rows_count_before = len(driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr"))
        driver.find_element_by_name("remove_cart_item").click()
        WebDriverWait(driver, 5).until(
            EC.staleness_of(product_row)
        )
        rows_count_after = len(driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr"))
        if i == 2:
            # last element, table is deleted
            assert rows_count_after == 0
        else:
            assert rows_count_after + 1 == rows_count_before
