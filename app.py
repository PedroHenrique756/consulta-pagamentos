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
    # Verificar se está "em dia" ou "atrasado"
    btn_pesquisar = drive.find_element(By.XPATH, "//button[@class='btn btn-custom btn-lg btn-block mt-3']")
    sleep(1)
    btn_pesquisar.click()
    sleep(4)

    status = drive.find_element(By.XPATH, "//span[@id='statusLabel']")
    if status.text == 'em dia':
        # Se estiver em dia, pegar a data do pagamento e o método do pagamento (cartão, boleto)
        data_pagamento = drive.find_element(By.XPATH, "//p[@id='paymentDate']")
        metodo_pagamento = drive.find_element(By.XPATH, "//p[@id='paymentMethod']")
    else:
        # Caso contrario (se estiver atrasado) coloque o status como pendente