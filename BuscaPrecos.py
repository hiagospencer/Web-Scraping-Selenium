
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

class WebScraping():
    """Class criada para fazer um WebScraping na página do Google Shopping. Criando um DataFrame e passando para um arquivo Excel.
    """
    
    def iniciar_programa(self):
        # Método de iniciar o programa.
        self.abrir_navegador('https://www.google.com/')
        self.pesquisando_produto(produto)
        self.raspando_nomes()
        self.raspando_precos()
        self.pegando_sites_produtos()
        self.criando_dataframe()
        self.passando_df_excel()
    
    def abrir_navegador(self,link_site):
        # Método de abrir o navegador, passando como parâmetro o link do Site.
        self.link_site = link_site 
        navegador.get(self.link_site)
        navegador.maximize_window()
    
    def pesquisando_produto(self,produto):
        # Método de fazer a pesquisa do produto. Passando como parâmetro o nome do produto para fazer a raspagem.
        self.produto = produto
        navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(produto)
        navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
        # Clicando no botão do shopping do google
        navegador.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
        print('Pesquisando o Produto.')
        
    def raspando_nomes(self):
        # Método para pegar todos os nomes do produtos selecionado pelo o Google. Retornando uma lista com os nomes dos Produtos.
        produtos = navegador.find_elements(By.CLASS_NAME, 'sh-np__product-title')
        lista_produtos = []
        for produto in produtos:
            lista_produtos.append(produto.text)
        print('Raspando os nomes dos produtos.')
        return lista_produtos
        
    def raspando_precos(self):
        # Método para pegar os preços dos produtos. Retornando os preços dos produtos.
        lista_preco = []
        precos = navegador.find_elements(By.CLASS_NAME, 'T14wmb')
        for preco in precos:
            lista_preco.append(preco.text)
        print('Raspando os Preços dos Produtos.')
        return lista_preco
    
    def pegando_sites_produtos(self):
        # Método para pegar os Site de cada produtos da pesquisa no Google Shopping. Retornando uma lista com os Sites.
        lista_site = []
        links = navegador.find_elements(By.CLASS_NAME, 'sh-np__click-target')
        for link in links:
            lista_site.append(link.get_attribute('href'))
        print('Pegando o site correspondente do Produtos.')
        return lista_site
            
    def criando_dataframe(self):
        # Método para criar um DataFrame com as lista de Produtos, Preços e Sites. Retornando o DataFrame
        global df_google
        lista_de_tuplas = list(zip(self.raspando_nomes(), self.raspando_precos(), self.pegando_sites_produtos()))
        df_google = pd.DataFrame(lista_de_tuplas, columns=['Produtos', 'Preços', 'Site'])
        print('Criando um DataFrame com os Nomes do Produtos, Preços e Site.')
        return df_google
    
    def passando_df_excel(self):
        # Método para passar o DataFrame para arquivo Excel.
        arquivo = 'ProdutosGoogle.xlsx'
        df_google.to_excel(arquivo)
        print('Passando o DataFrame para arquivo excell.')


produto = input('Qual o produto da pesquisa? ')

iniciar = WebScraping()
iniciar.iniciar_programa()
print('Fim do Programa!')
