import requests
import pandas as pd
#from IPython.display import display
from key import key_api  # pega a chave da api
from io  import StringIO # para fingir que uma string é um arquivo
 

#tickets = ['BBAS3','TAEE4','KLBN4','TRPL4','SANB4']
tickets = ['BBAS3','TAEE4']
compilada = pd.DataFrame()

for ticket in tickets:
  url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticket}.SAO&apikey={key_api}&datatype=csv'
  r = requests.get(url)
  tabela = pd.read_csv(StringIO(r.text))
  lista_tabelas = [compilada,tabela]
  compilada = pd.concat(lista_tabelas)

#display(compilada) 
df.style