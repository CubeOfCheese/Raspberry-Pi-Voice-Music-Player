from selenium import webdriver
import time

email = raw_input("Enter search: ")
password = raw_input("Enter password: ")
driver = webdriver.Firefox()
# driver.get('https://open.spotify.com/browse/featured')
# driver.switch_to.frame("app-player")
# play = driver.find_element_by_id("play-pause")
# play.click()
# driver.get('http://divercity-network.appspot.com/')
# search_bar = driver.find_element_by_id('search_bar')
# search_bar.send_keys(search)
# driver.get('https://open.spotify.com/browse/featured')
# time.sleep(10)
# log_in_button = driver.find_element_by_css_selector('button.btn.btn-black.btn--no-margin.btn--full-width.P7Qjj40AVoE8Igi7Ji05m._1xNlj_ScH8hEMWzrkRt1A')
# print log_in_button
# log_in_button.submit()
driver.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fbrowse%2Ffeatured')
time.sleep(10)
email_bar = driver.find_element_by_id('login-username')
password_bar = driver.find_element_by_id('login-password')
login_button = driver.find_element_by_css_selector('button#login-button.btn.btn-block.btn-green.ng-binding')

email_bar.send_keys(email)
password_bar.send_keys(password)
login_button.click()

# play_button.submit()
