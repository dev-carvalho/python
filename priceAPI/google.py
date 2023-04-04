# Importar a biblioteca pandas_datareader
import pandas_datareader as pdr

# Definir uma lista de códigos de ticker de ações
tickers = ["GOOG", "AAPL", "AMZN", "FB", "TSLA"]

# Definir a fonte de dados como "google"
data_source = "google"

# Iterar sobre a lista de códigos de ticker
for ticker in tickers:
    # Capturar os preços da ação
    df = pdr.DataReader(ticker, data_source)

    # Capturar o preço mais recente da ação
    price = df.tail(1)["Close"].iloc[0]

    # Imprimir o preço da ação na tela
    print(f"O preço atual da ação {ticker} é ${price:.2f}")
