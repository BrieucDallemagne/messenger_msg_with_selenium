from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome( options=options)
driver.get('https://www.messenger.com')

accept_cookies_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Autoriser tous les cookies']"))
)
accept_cookies_button.click()


email = "your_email"
password = "your_password"
victime = "victim_name"
message = "your_message"

email_input = driver.find_element(By.ID, 'email').send_keys(email)
password_input = driver.find_element(By.ID, 'pass').send_keys(password)
time.sleep(3)
login_button = driver.find_element(By.ID, 'loginbutton').click()

time.sleep(3)

driver.implicitly_wait(10)


search_box = driver.find_element(By.XPATH, "//input[@placeholder='Rechercher dans Messenger']")
search_box.send_keys(victime)
driver.implicitly_wait(10)
time.sleep(3)

click_victime = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[1]/div[2]/li[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
click_victime.click()

time.sleep(3)

#choose your loop
for i in range(10):
    chat_box = driver.find_element(By.XPATH, "//p[@class='xat24cr xdj266r']")
    chat_box.send_keys(message)
    time.sleep(1)

    chat_box.send_keys(Keys.ENTER)
    time.sleep(1)


driver.quit()