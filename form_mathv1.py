## Formulário
import requests
import json
from time import sleep
from email_sender import enviar_email

# Setando o link do banco de dados << Utilizei Firebase no Projeto # Nivaldo_Agradece

link = "https://form-70259-default-rtdb.firebaseio.com"

# Variáveis

email = str(input('Primeiramente nos informe seu em-mail: '))
nome = str(input("Informe seu nome: \n"))
Idade = str(input("Idade: \n"))
opn = str(input("Você gostou do formulário?\n"))


print('Enviando dados, aguarde.')
print('Aguarde')
print('=-' * 10)
for i in range(5, 0, -1):
    print(f'{i}sec.')
    sleep(1)
print('\nDados Enviados com Sucesso!')
print('=-' * 10)

user = nome.lower()


dados = (nome, opn, Idade)
requisicao = requests.post(f'{link}/forms/{user}.json', data=json.dumps(dados))
enviar_email()


print(requisicao)
print(requisicao.text)

