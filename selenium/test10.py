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
    driver.get("http://localhost/litecart/")
    WebDriverWait(driver, 10).until(EC.title_is(u"Online Store | My Store"))

    items = driver.find_element_by_id("box-campaigns")
    #item = items.find_element_by_tag_name("div").find_element_by_tag_name("ul").find_element_by_tag_name("li").find_element_by_tag_name("a")
    item = items.find_element_by_xpath("div//ul//li//a")
    print(item.get_attribute("title"))
    link = item.get_attribute("href")
    name_on_main = item.get_attribute("title")
    price_on_main_regular = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//s").get_attribute("textContent")
    price_on_main_campaign = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//strong").get_attribute("textContent")
    item.click()
    WebDriverWait(driver, 2).until(EC.title_is(u"Yellow Duck | Subcategory | Rubber Ducks | My Store"))
    print(driver.current_url)
    print(link)
    print(price_on_main_regular)
    print(price_on_main_campaign)
    assert driver.current_url == link

    product_name = driver.find_element_by_xpath("//div[@id='box-product']//div//h1")
    name_opened = product_name.get_attribute("textContent")
    print(name_on_main)
    print(name_opened)
    assert name_opened == name_on_main

    product_price_regular = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//s")
    price_regular = product_price_regular.get_attribute("textContent")
    print(price_regular)
    print(price_on_main_regular)
    assert price_regular == price_on_main_regular

    product_price_campaign = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//strong")
    price_campaign = product_price_campaign.get_attribute("textContent")
    print(price_campaign)
    print(product_price_campaign)
    assert price_campaign == price_on_main_campaign

    element.value_of_css_property(property_name)




