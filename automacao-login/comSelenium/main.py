from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configurações do Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service('/path/to/chromedriver')  # Atualize o caminho para o seu ChromeDriver

# Inicia o navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

# Função para realizar login e preencher formulário
def login_and_fill_form(url, login_info, form_data):
    driver.get(url)
    
    # Preenche os campos de login
    username_field = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')  # Atualize o XPath conforme necessário
    password_field = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')  # Atualize o XPath conforme necessário
    
    username_field.send_keys(login_info['08819186446'])
    password_field.send_keys(login_info['Gustavo30*'])
    password_field.send_keys(Keys.RETURN)  # Envia o formulário de login
    
    time.sleep(5)  # Aguarda o login ser processado
    
    # Preenche o formulário
    for field_xpath, value in form_data.items():
        field = driver.find_element(By.XPATH, field_xpath)  # Atualize o XPath conforme necessário
        field.send_keys(value)
    
    # Opcional: Envia o formulário
    # submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')  # Atualize o XPath conforme necessário
    # submit_button.click()

# Dados de login e formulário
login_info1 = {'username': 'user1', 'password': 'pass1'}
form_data1 = {'//input[@name="field1"]': 'value1', '//input[@name="field2"]': 'value2'}

# Primeiro site
login_and_fill_form('https://brpioneer.accenture.com/originacao-auto/login/sign-in', login_info1, form_data1)

# Abre uma nova aba e realiza a mesma operação
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

login_info2 = {'username': 'user2', 'password': 'pass2'}
form_data2 = {'//input[@name="field1"]': 'value3', '//input[@name="field2"]': 'value4'}

login_and_fill_form('https://site2.com/login', login_info2, form_data2)

# Finaliza o navegador após uma pausa
time.sleep(10)
driver.quit()
