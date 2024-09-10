from time import sleep
import re

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
urlget = 'https://www.tiktok.com/@user'
driver.get(urlget)
sleep(9)
actions = ActionChains(driver)
urls = []


try:
    for _ in range(100):
        url_actual = driver.current_url
        print(url_actual)
        urls.append(url_actual)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        sleep(1)

except KeyboardInterrupt:
    print("Detenido por el usuario.")

finally:
    user_name = re.search(r'@([^/]+)', urlget).group(1)
    print(user_name)
    name_file = f'{user_name}.txt'
    with open(name_file, 'w') as archivo:
        for url in urls:
            archivo.write(url + '\n')