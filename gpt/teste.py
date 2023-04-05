

import requests
from bs4 import BeautifulSoup

# Get the web page
url = 'https://www.poder360.com.br/'
page = requests.get(url)

# Parse the page
soup = BeautifulSoup(page.text, 'html.parser')

# Get all the headers
headers = soup.find_all('h1')

# Translate them to Spanish
spanish_headers = []
for header in headers:
    spanish_headers.append(header.get_text().translate(to='es'))

# Write the Spanish headers to a HTML file
with open('headers_spanish.html', 'w') as f:
    f.write('<html>\n')
    f.write('<head><title>Spanish Headers</title></head>\n')
    f.write('<body>\n')
    for header in spanish_headers:
        f.write('<h1>' + header + '</h1>\n')
    f.write('</body>\n')
    f.write('</html>\n')