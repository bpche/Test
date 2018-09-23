from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('http://automationpractice.com/index.php')

move(570, 826)
more_button = browser.find_element_by_xpath('xpath=//ul[@id='homefeatured']/li[2]/div/div[2]/div[2]/a[2]/span']
more_button.click()

