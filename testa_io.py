
arquivo = open('dados/contatos-escrita.csv', encoding='ISO-8859-1', mode='w')

# print(type(arquivo.buffer.read()))

texto_em_bytes = bytes('isso é um texto em bytes', encoding='ISO-8859-1')

# print(type(texto_em_bytes))
# print(texto_em_bytes)

contato = bytes('15,Verônica,veronica@veronica', encoding='ISO-8859-1')

arquivo.buffer.write(contato)

arquivo.close()