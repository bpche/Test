from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('http://automationpractice.com/index.php')

Button_shirt = browser.find_elements_by_link_text('T-Shirt')
Button_shirt.click()

Button_compare = browser.find_element_by_css_selector('p.compare')
Button_compare.click()
