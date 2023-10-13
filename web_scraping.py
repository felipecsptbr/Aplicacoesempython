import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações iniciais
URL = "https://www.amazon.com.br/s?k=pc+gamer&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=34JQB4CK7TUXU&sprefix=pc+gamer%2Caps%2C152&ref=nb_sb_noss_1"

# Inicialização do WebDriver
driver = webdriver.Chrome()
driver.get(URL)

# Espera explícita para garantir que os elementos estejam carregados
wait = WebDriverWait(driver, 10)

titulos = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
    )
)
precos = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//span[@class='a-price-whole']"))
)

# Criando e configurando a planilha
workbook = openpyxl.Workbook()
workbook.create_sheet("produtos")
sheet_produtos = workbook["produtos"]
sheet_produtos["A1"].value = "Produto"
sheet_produtos["B1"].value = "Preços"

# Inserindo títulos e preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])

workbook.save("produtos.xlsx")

# Fechando o navegador
driver.quit()
