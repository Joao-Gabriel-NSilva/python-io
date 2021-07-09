
arquivos_contato = open('dados/contatos-escrita.csv', encoding='UTF-8', mode='w+')

contatos = ['11,Carol,carol@carol.com.br\n', '12,Ana,ana@ana.com.br\n', '13,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']


for contato in contatos:
    arquivos_contato.write(contato)

arquivos_contato.flush()

arquivos_contato.seek(0)

for contato in arquivos_contato:
    print(contato, end='')

