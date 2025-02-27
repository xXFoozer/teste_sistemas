from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

time.sleep(5)
navegador.maximize_window()
navegador.get("https://www.facebook.com/")
time.sleep(5)
navegador.find_element(By.NAME, "email").send_keys("gemanorodriguesgomes@gmail.com")
navegador.find_element(By.NAME, "pass").send_keys("456789")
time.sleep(5)
botao_verde = navegador.find_element(By.NAME,value= 'login')
botao_verde.click()
time.sleep(5)

