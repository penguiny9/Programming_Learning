
# coding=UTF-8
#!/usr/bin/env python3
from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get('https://mail.163.com')
linkElem=browser.find_element_by_link_text('密码登录')
linkElem.click()

time.sleep(5)
browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
emailElem=browser.find_element_by_name("email")
emailElem.send_keys('peitan1989')
passwordElem=browser.find_element_by_name("password")
passwordElem.send_keys('112358Penny')
browser.find_element_by_id('dologin').click()