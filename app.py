import random

# Criação das listas que servirão como fonte.
nomes = ['Wevanny', 'Dalila', 'Liam', 'Bisnarga', 'Sharapova']
e_mails = ['wevanny@gmail.com', 'dalila@gmail.com', 'liam@gmail.com', 'bisnarga@gmail.com',
           'sharapova@gmail.com']
telefones = ['82987555035', '82987657522', '82987555036', '82987657512', '82987555050']
cidades = ['Saint John', 'Miramichi','Moncton', 'Fredericton', 'Airdrie']
provincias = ['New Brunswick', 'Alberta', 'Ontario', 'Nova Scotia', 'Quebec']

# Abrindo o arquivo para a escrita no modo append.
arquivo = open('dados.txt', 'a')

# Loop para continuidade da execução até o pedido de 'parar'
while True:
    # Boas-vindas e rápida instrução.
    print('----------------------------------------------------------------------------------')
    print('Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa digite "parar"')
    print('----------------------------------------------------------------------------------')
    
    # Opções fornecidas ao usuário.
    escolha = input('Escolha uma ou mais opções abaixo a serem geradas ' 
                'aleatoriamente \n[1] - Nome \n[2] - E-mail \n[3] - Telefone \n[4] - Cidade \n[5] - Província'
                '\nDigite uma ou mais opções: ')
    
    # Verificando comando de parada.
    if escolha.lower() == 'parar':
        print('Programa Encerrado.')
        break

    # Fornecimento de opção pora salvar em arquivo de texto.
    salvar_arquivo = input('Gostaria de salvar os dados em um arquivo de texto?(s/n): ')   
    
    # Separação das opções digitadas pelo usuário.
    opcoes = escolha.split(',')

    # Lista para os dados gerados.
    dados_gerados = []

    # Laço de repetição para escolha das opções. 
    for opcao in opcoes:
        # Verificando se cada uma das opções pertence a um conjunto válido.
        if opcao.strip() in ['1', '2', '3', '4', '5']:
            if opcao.strip() == '1':
                # Selecionar um nome aleatório da lista 'nomes'.
                nome_aleatorio = random.choice(nomes)
                print(nome_aleatorio)
                dados_gerados.append(nome_aleatorio)
            elif opcao.strip() == '2':
                # Selecionar um nome aleatório da lista 'e_mails'.
                email_aleatorio = random.choice(e_mails)
                print(email_aleatorio)
                dados_gerados.append(email_aleatorio) 
            elif opcao.strip() == '3':
                # Selecionar um nome aleatório da lista 'telefones'.
                telefone_aleatorio = random.choice(telefones)
                print(telefone_aleatorio)
                dados_gerados.append(telefone_aleatorio) 
            elif opcao.strip() == '4':
                # Selecionar um nome aleatório da lista 'cidades'.
                cidade_aleatoria = random.choice(cidades)
                print(cidade_aleatoria)
                dados_gerados.append(cidade_aleatoria)  
            elif opcao.strip() == '5':
                # Selecionar um nome aleatório da lista 'provincias'.
                provincia_aleatoria = random.choice(provincias)
                print(provincia_aleatoria)
                dados_gerados.append(provincia_aleatoria)  
            else:
                print('Opção inválida:', opcao)
   
    # Verificando se o usuário deseja salvar.
    if salvar_arquivo.lower() == 's':
        with open('dados.txt', 'a') as arquivo:
            for dado in dados_gerados:
                arquivo.write(dado + '\n')

    # Dando a opção de limpar ou não a lista.
    limpar_lista = input('Deseja limpar a lista para a próxima iteração?(s/n): ')
    if limpar_lista.lower() == 's':
        # Abrindo em modo de gravação.
        with open('dados.txt', 'w') as arquivo:
            # Limpando o conteúdo do arquivo.
            arquivo.write('')

        # Limpando a lista de dados.    
        dados_gerados.clear()

# Fechando o arquivo ao término do laço de repetição.
arquivo.close()


