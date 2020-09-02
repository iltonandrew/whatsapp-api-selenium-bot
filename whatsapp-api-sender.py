from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# As unicas coisas que tem que mudar:

text = "Hello%20there!"


# Whatsapp number in 14 digit format
numbers = ['00000000000000', '11111111111111']


driver = webdriver.Chrome('chromedriver.exe')

for number in numbers:

    driver.get("https://wa.me/"+number+"?text=" + text)
    wait = WebDriverWait(driver, 30)

    time.sleep(15)
    x_arg = '//*[@id="action-button"]'
    continue_box = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    continue_box.click()
    time.sleep(7)

    web_text = '//*[@id="fallback_block"]/div/div/a'
    use_web = wait.until(EC.presence_of_element_located((
        By.XPATH, web_text)))
    use_web.click()
    time.sleep(7)

    actions = ActionChains(driver)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(10)


driver.close()

print("Messages sent!")
