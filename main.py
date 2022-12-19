import requests

# URL do serviço de cotação de moedas do Yahoo Finance
url = 'https://finance.yahoo.com/quote/BRL=X'

# Fazendo uma requisição GET para a URL
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
  # Convertendo o conteúdo da página em um objeto BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')

  # Procurando a cotação atual do dólar
  cotacao = soup.find('div', class_='D(ib) Fw(200)')

  # Imprimindo a cotação encontrada
  print(cotacao.text)
else:
  print('Erro ao acessar o site')
