<h1>📗 Sobre</h1>
<p>Este projeto automatiza a consulta do status de pagamento de clientes a partir de um arquivo Excel (dados_clientes.xlsx). O script utiliza Selenium para acessar um site de verificação de CPF, extrair informações sobre o status de pagamento e registrar os resultados em um segundo arquivo Excel (planilha fechamento.xlsx).</p>

<h1>💻 Funcionalidades</h1>
<p>1. Abre o arquivo dados_clientes.xlsx e extrai os CPFs.</p>
<p>2. Acessa o site https://consultcpf-devaprender.netlify.app/ via Selenium.</p>
<p>3. Insere o CPF e verifica o status.</p>
<p>4. Se estiver "em dia", salva a data e o método de pagamento em planilha fechamento.xlsx.</p>
<p>5. Se estiver "pendente", apenas registra essa informação.</p>
<p>6. Salva e fecha os arquivos Excel.</p>

<h1>Como usar</h1>
<p>1. Preencha a planilha de clientes (dados_clientes.xlsx****)</p>
<p>*O arquivo deve conter as colunas: Nome, Valor, CPF, Vencimento.</p>
<p>Execute o script</p>
<p>*app.py</p>
<p>3.Verifique o resultado</p>
<p>*Os dados serão salvos em planilha fechamento.xlsx, com o status "em dia" ou "pendente".</p>


<h1>🚀 Tecnologias usadas</h1>
<p>- Python</p>
<p>- OpePython</p>
<p>- nPyXL</p>

<h1>Autor</h1>
<p>Pedro Henrique Gudes de Araujo</p>
