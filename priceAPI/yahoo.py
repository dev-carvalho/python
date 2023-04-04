
# escreva um programa comentado em python para capturar preço de acoes na yahoo finance


# Importar a biblioteca yfinance
import yfinance as yf

# Definir uma lista de ações para acompanhar
tickers = ["PETR4.SA", "BBAS3.SA", "TAEE4.SA", "TAEE3.SA", "PETR4.SA", "BBAS3.SA", "TAEE4.SA", "TAEE3.SA"]

# Iterar sobre a lista de ações
for ticker in tickers:
    # Capturar o objeto correspondente a ação
    stock = yf.Ticker(ticker)

    # Capturar o preço atual da ação
    price = stock.info["regularMarketPrice"]

    # Imprimir o preço da ação na tela
    print(f"O preço atual da ação {ticker} é ${price:.2f}")