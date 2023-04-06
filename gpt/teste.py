

import requests
from bs4 import BeautifulSoup

# URL da página web
url = 'https://www.example.com/'

# Fazendo uma solicitação à página web
resposta = requests.get(url)

# Extraindo o conteúdo HTML da resposta
html = resposta.content

# Criando um objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extraindo todos os headers HTML
headers = soup.find_all('h1')

# Traduzindo os headers para o espanhol
translated_headers = []
for header in headers:
    translated_header = header.text.replace('English', 'Espanhol')
    translated_headers.append(translated_header)

# Gravando o resultado no arquivo HTML
with open('resultado.html', 'w') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>Resultado</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    for header in translated_headers:
        f.write('<h1>{}</h1>\n'.format(header))
    f.write('</body>\n')
    f.write('</html>\n')