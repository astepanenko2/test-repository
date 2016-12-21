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


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class ItemPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.current_count = 0

    def add_to_cart(self):
        if self.driver.find_elements_by_name("options[Size]"):
            self.driver.find_element_by_xpath("//select[@name='options[Size]']/option[text()='Large +$5']").click()
        self.driver.find_element_by_name("add_cart_product").click()
        self.current_count += 1

    def wait_for_counter(self):
        WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@id='cart']//a[@class='content']//span[@class='quantity']"),
                str(self.current_count)
            )
        )

    def back_to_main(self):
        self.driver.find_element_by_xpath("//i[contains(@class, 'fa-home')]").click()


class CartPage(BasePage):

    def remove_item(self):
        self.product_row = self.driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr")[1]
        self.rows_count_before = len(self.driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr"))
        self.driver.find_element_by_name("remove_cart_item").click()

    def wait_and_check_remove(self, is_last):
        WebDriverWait(self.driver, 5).until(
            EC.staleness_of(self.product_row)
        )
        rows_count_after = len(self.driver.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr"))
        if is_last:
            # last element, table is deleted
            assert rows_count_after == 0
        else:
            assert rows_count_after + 1 == self.rows_count_before


class MainPage(BasePage):

    def open_main(self):
        self.driver.get("http://localhost/litecart/en/")
        WebDriverWait(self.driver, 10).until(EC.title_is(u"Online Store | My Store"))

    def get_product_list(self):
        product_list = self.driver.find_elements_by_xpath("//div[@id='box-latest-products']//li[contains(@class, 'product')]")
        assert len(product_list) > 0
        return product_list

    def open_product(self, idx):
        product_list = self.get_product_list()
        product = product_list[idx]
        product.find_element_by_xpath("a[contains(@class, 'link')]").click()

    def open_cart(self):
        self.driver.find_element_by_xpath("//div[@id='cart']//a[@class='link']").click()


def test_menu(driver):

    item_page = ItemPage(driver)
    cart_page = CartPage(driver)
    main_page = MainPage(driver)

    # main page open
    main_page.open_main()

    for idx in range(3):
        # choose item
        main_page.open_product(idx)

        item_page.add_to_cart()
        item_page.wait_for_counter()
        item_page.back_to_main()

    main_page.open_cart()

    for i in range(3):
        cart_page.remove_item()

        if i == 2:
            is_last = True
        else:
            is_last = False
        cart_page.wait_and_check_remove(is_last)
