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
    font_size_on_main_regular = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//s").value_of_css_property("font-size")
    color_on_main_regular = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//s").value_of_css_property("color")
    text_decoration_on_main_regular = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//s").value_of_css_property("text-decoration")
    font_size_on_main_campaign = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//strong").value_of_css_property("font-size")
    color_on_main_campaign = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//strong").value_of_css_property("color")
    text_decoration_on_main_campaign = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//strong").value_of_css_property("font-weight")
    item.click()
    WebDriverWait(driver, 2).until(EC.title_is(u"Yellow Duck | Subcategory | Rubber Ducks | My Store"))

    assert driver.current_url == link
    assert float(font_size_on_main_campaign[:-2]) > float(font_size_on_main_regular[:-2])
    assert color_on_main_regular == "rgba(119, 119, 119, 1)"
    assert color_on_main_campaign == "rgba(204, 0, 0, 1)"
    assert text_decoration_on_main_regular == "line-through"
    assert text_decoration_on_main_campaign == "bold"

    product_name = driver.find_element_by_xpath("//div[@id='box-product']//div//h1")
    name_opened = product_name.get_attribute("textContent")
    assert name_opened == name_on_main

    product_regular = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//s")
    price_regular = product_regular.get_attribute("textContent")
    font_size_regular = product_regular.value_of_css_property("font-size")
    color_regular = product_regular.value_of_css_property("color")
    text_decoration_regular = product_regular.value_of_css_property("text-decoration")
    assert price_regular == price_on_main_regular
    assert text_decoration_regular == "line-through"
    assert color_regular == "rgba(102, 102, 102, 1)"

    product_campaign = driver.find_element_by_xpath("//div[contains(@class, 'price-wrapper')]//strong")
    price_campaign = product_campaign.get_attribute("textContent")
    font_size_campaign = product_campaign.value_of_css_property("font-size")
    color_campaign = product_campaign.value_of_css_property("color")
    text_decoration_campaign = product_campaign.value_of_css_property("font-weight")
    assert price_campaign == price_on_main_campaign
    assert font_size_campaign > font_size_regular
    assert text_decoration_campaign == "bold"
    assert color_campaign == "rgba(204, 0, 0, 1)"





