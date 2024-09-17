from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) # headless
    pagina = navegador.new_page()
    pagina.goto("https://brpioneer.accenture.com/originacao-auto/login/sign-in")
    pagina.fill('xpath=//*[@id="mat-input-0"]', "08819186446")
    pagina.fill('xpath=//*[@id="mat-input-1"]', 'Gustavo30*')
    pagina.locator('xpath=/html/body/app-root/div/div/app-sign-in-container/div/div[2]/div/div/form/div[5]/button').click()
    time.sleep(100)