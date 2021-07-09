
contato_carol = '11,Carol,carol@carol.com.br'
contato_andressa = '12,Andressa,andressa@andressa.com.br'

with open('dados\contatos-escrita.csv', encoding='UTF-8', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open('dados\contatos-escrita.csv', encoding='UTF-8', mode='w') as arquivo2:
    arquivo2.write(contato_andressa)





