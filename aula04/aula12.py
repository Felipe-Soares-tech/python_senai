import requests
cep = 72154214
link = f'URL: viacep.com.br/ws/{cep}/json/'
endereco = requests.get(link)
print(endereco)