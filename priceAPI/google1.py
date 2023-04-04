# Importar as bibliotecas necessárias
import yfinance as yf
import pandas as pd

# Criar um dicionário com os códigos das ações e seus respectivos nomes
stocks = {
    'GOOG': 'Google',
    'AAPL': 'Apple',
    'AMZN': 'Amazon',
    'FB': 'Facebook',
    'TSLA': 'Tesla'
}

# Criar um DataFrame vazio para armazenar os preços das ações
prices_df = pd.DataFrame(columns=['Nome', 'Código', 'Preço'])

# Iterar sobre o dicionário de ações
for code, name in stocks.items():
    # Obter os dados da ação usando a biblioteca yfinance
    stock_data = yf.Ticker(code).history(period='1d')

    # Obter o preço da ação mais recente
    latest_price = stock_data.iloc[-1]['Close']

    # Adicionar o preço da ação ao DataFrame
    prices_df = prices_df.append({
        'Nome': name,
        'Código': code,
        'Preço': latest_price
    }, ignore_index=True)

# Exibir o DataFrame com os preços das ações
print(prices_df)
