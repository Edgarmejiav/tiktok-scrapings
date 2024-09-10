from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from helps import read_file_to_list

filename = ".ac_edits13.txt"
result = read_file_to_list(filename)

driver = webdriver.Chrome()
urlget = 'https://www.sssstik.com/es/'
driver.get(urlget)

input_field = driver.find_element(By.CLASS_NAME, "functionAreaInput")


for index, url in enumerate(result):
    print(index)
    input_field.send_keys(url)
    input_value = input_field.get_attribute("value")
    sleep(1)
    download_button = driver.find_element(By.CLASS_NAME, "functionAreaBtn")
    download_button.click()
    sleep(5)
    mp4_option = driver.find_element(By.XPATH, "//div[text()='MP4 sin marca de agua']")
    mp4_option.click()

sleep(99)
