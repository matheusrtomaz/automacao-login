from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get('https://brpioneer.accenture.com/originacao-auto/login/sign-in')
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys('08819186446')
navegador.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys('Gustavo30*')

time.sleep(1000)