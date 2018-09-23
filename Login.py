from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('http://automationpractice.com/index.php')

button_sign = browser.find_elements_by_link_text('Sign in')
button_sign.click()

signup_email = browser.find_element_by_id('id_email')
signup_password = browser.find_element_by_id('id_passwd')
signup_button = browser.find_element_by_css_selector('#SubmitLogin > span')

signup_email.send_keys('bambang.prasetyo085@gmail.com')
signup_password.send_keys('Gameloft01')

signup_button.click()
