from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

#Open Browser
browser.get('https://twitter.com/login')

#Get Email Input
email = browser.find_element_by_class_name('js-username-field')
#Put in Email
email.send_keys('example@company.com')

#Get Password Input
password = browser.find_element_by_class_name('js-password-field')
#Put in Password
password.send_keys('Pa$$w0rd')

#Press ENTER
password.send_keys(Keys.ENTER)