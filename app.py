import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Entrar na planilha e extrair o CPF do cliente
planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_clientes = planilha_clientes['Sheet1']

drive = webdriver.Chrome()
drive.get('https://consultcpf-devaprender.netlify.app/')
for linha in pagina_clientes.iter_rows(min_row=2, values_only=True):
    nome, valor, cpf, vencimento = linha
    # Entra no verificador de cpf
    sleep(5)
    campo_pesquisa = drive.find_element(By.XPATH, "//input[@id='cpfInput']")
    sleep(1)
    campo_pesquisa.send_keys(cpf)
