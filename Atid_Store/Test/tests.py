import time

# import sys
# sys.path.insert(0,"C:\Users\user\PycharmProjects\Mini_Project_Selenium\Atid_Store\Base_Tast\Locators.py")
from Atid_Store.Base_Tast.Locators import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# @pytest.mark.Skip
def test_store_product():
    driver.get(locator)
    driver.maximize_window()
    driver.find_element(By.XPATH, locator1).click()
    time.sleep(2)
    driver.find_element(By.XPATH, locator2).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator3 ).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator4).click()
    time.sleep(2)
    product_name = driver.find_element(By.XPATH,locator5).text
    assert locator6 == product_name
    time.sleep(2)
def test_Man_product():
    driver.get(locator)
    driver.maximize_window()
    driver.find_element(By.XPATH,locator11).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator22).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator33).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator44).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator55).click()
    time.sleep(2)
    product_name=driver.find_element(By.XPATH,locator66).text
    assert locator77 == product_name
def test_Women_product():
    driver.get(locator)
    driver.maximize_window()
    driver.find_element(By.XPATH,locator12).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator13).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator14).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator15).click()
    time.sleep(2)
    product_name3=driver.find_element(By.XPATH,locator16).text
    assert locator17 == product_name3
def test_Acecceries_product():
    driver.get(locator)
    driver.maximize_window()
    driver.find_element(By.XPATH,locator18).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator19).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator20).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locator21).click()
    time.sleep(2)
    coupon_field=driver.find_element(By.XPATH,locator222)
    coupon_field.clear()
    coupon_field.send_keys(locator34)
    time.sleep(2)
    driver.find_element(By.XPATH,locator35).click()
    time.sleep(2)
    product_name2 = driver.find_element(By.XPATH,locator36).text
    assert locator37==product_name2