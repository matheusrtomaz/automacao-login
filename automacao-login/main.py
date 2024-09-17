from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Primeira aba - Primeiro site
    page1 = context.new_page()
    page1.goto("https://brpioneer.accenture.com/originacao-auto/login/sign-in")

    # Preencher login e senha
    page1.fill('//*[@id="mat-input-0"]', '08819186446')
    page1.fill('//*[@id="mat-input-1"]', 'Gustavo30*')
    page1.click('/html/body/app-root/div/div/app-sign-in-container/div/div[2]/div/div/form/div[5]/button')
    
    # Fechar o navegador
    browser.close()