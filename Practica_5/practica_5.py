from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(executable_path = "C:/Users\manub\Documents/7mo Semestre\PACS\chromedriver_win32/chromedriver.exe")
driver.get("https://demoblaze.com/")

#Registro de cuenta

driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID, "signin2").click()
time.sleep(2)

user_1 = driver.find_element(By.ID, "sign-username")
time.sleep(2)
user_1.send_keys("ManuelF4b")
time.sleep(2)

password_1 = driver.find_element(By.ID, "sign-password")
time.sleep(2)
password_1.send_keys("123456")
time.sleep(2)

driver.find_element(By.XPATH, '//[@id="signInModal"]/div/div/div[3]/button[2]').click()
time.sleep(2)

alert = Alert(driver)
alert.accept()
time.sleep(2)

driver.find_element(By.XPATH, ('//[@id="signInModal"]/div/div/div[3]/button[1]')).click()
time.sleep(2)

#Ingresar con cuenta

user = driver.find_element(By.ID, "loginusername")
time.sleep(2)
user.send_keys("ManuelF4b")
time.sleep(2)

password = driver.find_element(By.ID, "loginpassword")
time.sleep(2)
password.send_keys("123456")
time.sleep(2)

#Agregar elementos al carrito