import contato_utils

try:
    # contatos = contato_utils.csv_para_contatos('dados/contatos.csv')
    # contato_utils.contatos_para_pickle(contatos, 'dados/contatos.pickle')

    # contatos = contato_utils.pickle_para_contatos('dados/contatos.pickle')
    # contato_utils.contatos_para_json(contatos, 'dados/contatos.json')

    contatos = contato_utils.json_para_contatos('dados/contatos.json')

    for contato in contatos:
        print('{} - {} - {}'.format(contato.id, contato.nome, contato.email))

except FileNotFoundError:
    print('Arquivo não encontrado')

except PermissionError:
    print('Sem permissão de escrita')
