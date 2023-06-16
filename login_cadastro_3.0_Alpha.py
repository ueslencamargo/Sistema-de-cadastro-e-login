from mysql.connector import connect # o connect vai conectar ao banco de dados e executar os comandos necessários.
from os import system # importei o system para limpar a tela com 'cls'.
from colorama import Fore #colorir a fonte
import time

def menu_opcao():# Menu inicial, com as opções.

    MENU = 'on' # Criei essa variável para ativar o meu while, é como um botão liga e desliga.

    while MENU == 'on': # Enquanto estiver ligado, vai continuar exibindo o menu com as opções.

        print(Fore.GREEN +  '\nEscolha, fazer login ou novo cadastro?\n')
        print('1 - Fazer Login\n')
        print('2 - Novo Cadastro\n')
        print('3 - Sair\n')
        print('4 - Recuperar/Atualizar Senha\n')

        opcao = input('Digite sua opção e tecle Enter:') # A variável opcao recebe a escolha do usuário.

        match opcao:

            case '1' :
                system('cls') # Limpa o prompt.
                print(Fore.YELLOW + '* Login *') # Exibe  na tela a função escolhida.
                MENU = 'off'# (Desliga) o menu.
                command = login() # Chama a função para realizar o login.

            case '2' :
                system('cls')
                print(Fore.YELLOW + '* Cadastro *')
                command = cadastro()

            case '3' :
                system('cls')
                print(Fore.YELLOW + '* Sair *\n')
                print(Fore.RED+'Software encerrado.\n')
                quit() # Fecha o programa.

            case '4' :
                system('cls')
                print(Fore.YELLOW +'* Recuperar/Alterar Senha *')
                command = recuperar()

            case _: # Quando for digitado algo que não seja 1,2 ou 3.
                system('cls') # Vai limpar a tela.
                print(Fore.RED +'\n**Opção incorreta! Escolha 1 , 2, 3 ou 4.**')# Mostrar mensagem de erro e continua a exibir o menu.

def login():# Realizar o login.
    import stdiomask

    LOGIN = 'on' # Enquanto estiver (ligado) vai continuar pedindo o nome de usuário.
    SENHA = 'off' # Quando (ligado) vai pedir a senha.

    tentativas = 3 # Quando o usuário errar a senha ele terá mais algumas tentativas.

    conn = connect(host='localhost',user='root',password='sucata',database='cadastro') # Conectando com o banco de dados.
    cursor = conn.cursor()# Abrindo cursor ou Query para receber o comando mysql.

    while LOGIN == 'on': # Iniciando o loop que pede o nome de usuário.

        nome_digitado = input(Fore.GREEN + '\n Digite o seu nome de usuário:\n') # A variável recebe o nome digitado.

        cursor.execute("SELECT usuario FROM usuarios where usuario = '{}'".format(nome_digitado))# Verifica o nome no banco de dados.
        
        usuario = cursor.fetchone() # A variável recebe a verificação.

        if usuario is not None and nome_digitado == usuario[0]: # Se a verificação não estiver vazia e o nome digitado for correto.
                                                                # usuario na posição [0], que é a primeira posição da verificação.
            system('cls')                                       # colocando[0] também remove as vírgulas e parênteses.
            print('\nUsuário Ok!\n')
            print('Bom te ver de novo',nome_digitado,'\n')
            LOGIN = 'off'
            SENHA = 'on'
        
        else: # Aqui se a verificação não encontrar o nome digitado, vai limpar a tela e pedir de novo.
            system('cls')
            print(Fore.RED + '',nome_digitado,'não encontrado.')# Exibindo a mensagem de que o nome não foi encontrado.

    while SENHA == 'on' and tentativas >= 1: # Aqui vai pedir a senha enquanto ela estiver 'on' e as tentativas não estiverem zeradas.
            
        senha_digitada = stdiomask.getpass(prompt= Fore.GREEN + 'Digite sua senha:\n', mask='*')# Variável que recebe a senha digitada.

        cursor.execute("select senha from usuarios where usuario = '{}'".format(nome_digitado))# Vai buscar a senha do usuário no banco de dados.

        senha = cursor.fetchone() # A variável recebe a senha que foi buscada.

        if senha is not None and senha_digitada == senha[0]: # Se a busca não estiver vazia e a senha digitada corresponder com a busca.

            cursor.close() # Encerra o cursor pois não vai ser mais usado.
            conn.close() # Fecha a conexão com o banco de dados.
            system('cls')
            print(Fore.GREEN + '\nSenha Ok!\n')
            time.sleep(2)
            SENHA = 'off'
            system('cls')

            pisca = 3

            while pisca > 0 :
                print('\nLogin realizado com sucesso!\n')
                time.sleep(0.2)
                system('cls')
                print(Fore.GREEN +'\nLogin realizado com sucesso!\n')
                time.sleep(0.2)
                system('cls')
                print(Fore.RED +'\nLogin realizado com sucesso!\n')
                time.sleep(0.2)
                system('cls')
                print(Fore.YELLOW +'\nLogin realizado com sucesso!\n')
                time.sleep(0.2)
                system('cls')
                print(Fore.BLUE +'\nLogin realizado com sucesso!\n')
                time.sleep(0.2)
                system('cls')
                pisca = pisca - 1

            # Não temos nenhuma outra função para colocar aqui, então, encerramos.

        else: # Aqui se a senha não corresponder.
            tentativas = tentativas -1 # Vai diminuir as tentativas.
            system('cls')
            print(Fore.RED + '\nErro, tentativas restantes:', tentativas,'\n') # Exibir a mensagem de erro e continuar a pedir senha pois ainda está on.
        
        if tentativas == 0 : # Quando terminar as tentativas.
                system('cls')
                print(Fore.RED + '\nLimite de tentativas atingido!\n')
                print(Fore.GREEN + 'Software encerrado.\n')
                quit()# Fecha o programa.

def verificador_senha(R,EMAIL):# Verificar o tamanho da senha, vai servir também para recuperar
    
    import re # Lê os caracteres dentro de uma variável
    import stdiomask # Mascara a senha.

    verificar = 'on'
    confirmar = 'off'

    while verificar == 'on':
            
        print(Fore.GREEN + '\nA senha deve ter no mínimo 8 caracteres, conter pelo menos 1 número e 1 caractere especial.\n')

        senha_digitada = stdiomask.getpass(Fore.GREEN + 'Digite sua senha:\n')
        system('cls')

        if re.search(r'[!@#$%^&*(),.?":{}|<>]', senha_digitada) and re.search(r'\d', senha_digitada) and len(senha_digitada) >= 8:
            system('cls')
            print('\nCaracterer especial Ok')
            print('\nDigito Ok\n')
            print(len(senha_digitada),'caracteres Ok\n')
            verificar = 'off'
            confirmar = 'on'

        else:
            if (re.search(r'[!@#$%^&*(),.?":{}|<>]', senha_digitada)) == None:
                print(Fore.RED + 'Falta um caracter especial.')
            if (re.search(r'\d', senha_digitada)) == None:
                print(Fore.RED +'Falta um número.')
            if (len(senha_digitada)) < 8:
                print(Fore.RED +'Possui apenas',len(senha_digitada),'caracteres.')

    while confirmar == 'on':
            
            senhacon = stdiomask.getpass(prompt='Confirme sua senha:\n', mask='*')# Outra variável que recebe a senha para confirmar.

            if senhacon == senha_digitada: # Compara as senhas digitadas se forem iguais, inicia o loop para o e-mail.
                confirmar = 'off'
                system('cls')
                print(Fore.GREEN +'\n Caracterer especial',Fore.YELLOW +'Ok')
                time.sleep(1)
                print(Fore.GREEN +'\n Digito',Fore.YELLOW +'Ok\n')
                time.sleep(1)
                print(Fore.GREEN +'',len(senha_digitada),'caracteres',Fore.YELLOW +'Ok\n')
                time.sleep(1)
                print(Fore.GREEN +' Confirmação',Fore.YELLOW +'Ok\n')
                time.sleep(2)
                system('cls')

            else: # Aqui se as senhas digitadas não forem iguais, vai pedir a senha novamente.
                system('cls')
                print(Fore.RED + '\nA senha não confere.\n')
    
    while R == 'on':# Quando o R estiver ligado ou seja on vai ativar a recuperação da senha que vai atualizar o bd.

        conn = connect(host='localhost',user='root',password='sucata',database='cadastro') # Conectando com o banco de dados.
        cursor = conn.cursor()# Abrindo cursor ou Query para receber o comando mysql.
        cursor.execute("update usuarios set senha = '{}' where email = '{}'".format(senha_digitada,EMAIL))
        cursor.close()
        conn.close()
        system('cls')
        print('\n Senha atualizada com sucesso!')
        R = 'off'
        time.sleep(5)
    
    return senha_digitada# aqui a senha retorna, para usar no cadastro e não na recuperação.

def cadastro(): # Realizar novo cadastro.

    R =  'off' #Recuperar?
    NOME = 'on' # Enquanto estiver 'on' vai pedir nome de usuário.
    SENHA = 'off' # Quando 'on' pede a senha.
    EMAIL = 'off'# Quando 'on' pede o e-mail.
    INSERIR = 'off' # Quando on, ativa o loop de inseção no banco de dados.

    conn = connect(host='localhost',user='root',password='sucata',database='cadastro')# Conecta ao banco de dados.
    cursor = conn.cursor()# Abre um cursor ou Query.

    while NOME == 'on': # Inicia o loop para pedir um nome de usuário.

        novo_usuario = input(Fore.GREEN + '\nDigite um nome de usuario, deve ter no mínimo 3 caracteres e no máximo 6:\n')# Variável recebe o nome digitado.

        cursor.execute("SELECT usuario FROM usuarios where usuario = '{}'".format(novo_usuario))# Verifica se não tem nenhum nome igual no banco de dados.

        usuarios = cursor.fetchone()# Armazena a verificação.

        if usuarios is not None and novo_usuario == usuarios[0]:# Se a verificação voltar com um nome igual.
            system('cls')# Limpa a tela.
            print(Fore.RED + 'O nome',novo_usuario, 'já está cadastrado!')# Exibe a mensagem de que o nome já existe.
        
        elif len(novo_usuario) < 3 or len(novo_usuario) > 6:
            system('cls')
            print(Fore.RED + 'O nome é menor que 3 caracteres ou maior que 6 caracteres.') 
        
        else:# Aqui se o nome não existe, vai parar de pedir o nome, limpar a tela e ativar o loop da senha.
            NOME = 'off'
            system('cls')
            senha_digitada = verificador_senha(R,EMAIL)#executa a função para verificar a senha 
            system('cls')                                   #a senha digitada vai ser o return da função
            EMAIL = 'on'

    while EMAIL == 'on':

        print(Fore.GREEN + '\n',novo_usuario,'é importante que o seu e-mail seja válido!\n')

        print(Fore.RED +'Caso contrário não irá conseguir atualizar ou recuperar a senha!')
        
        email_digitado = input(Fore.GREEN +'\n Digite um e-mail de recuperação:\n') # Variável que recebe o e-mail digitado.

        cursor.execute("SELECT email FROM usuarios where email = '{}'".format(email_digitado))# Varifica se o e-mail está cadastrado.

        emails = cursor.fetchone() # Variável recebe a verificação.

        if  emails is not None and email_digitado == emails[0]:# Se o e-mail digitado já estiver cadastrado.
            system('cls')# Vai limpar a tela.
            print(Fore.RED + '\n O e-mail:',email_digitado, 'já está cadastrado!') # Avisar que o e-mail já está no banco de dados e continuar a pedir e-mail.
        
        else: # Aqui se o e-mail já não estiver cadastrado, limpa a tela e para o loop de pedir e-mail.
            EMAIL = 'off'
            INSERIR = 'on'

        while INSERIR == 'on': # Mostrar na tela a confirmação para realizar o cadastro.
            system('cls')
            print(Fore.YELLOW + '\nConfirma o cadastro?\n')
            print('Usuário:',novo_usuario)
            print('\nSenha:','*'*len(senha_digitada))
            print('\nE-mail:',email_digitado)
            
            confirmar = input('\n1 - Sim          2 - Não\n')# Variável que recebe a confirmação.
            
            if confirmar == '1':
                cursor.execute("INSERT INTO usuarios (usuario, senha, email) VALUES ('{}', '{}', '{}')".format(novo_usuario,senha_digitada,email_digitado))
                cursor.close() # Encerra o cursor pois não vai ser mais usado.
                conn.close() # Fecha a conexão com o banco de dados.
                system('cls')
                print('\nCadastro realizado com sucesso!\n')
                print('Agora você já pode fazer login.')
                INSERIR ='off'
                command = menu_opcao()
            if confirmar == '2':
                INSERIR = 'off'
                system('cls')
                command = menu_opcao()
            else:
                system('cls')
                print('\nOpção incorreta.\n')

def recuperar():# Inicia a recuperação da senha

    EMAIL = 'on'
    USUARIO = 'off'

    conn = connect(host='localhost',user='root',password='sucata',database='cadastro')# Conecta ao banco de dados.
    cursor = conn.cursor()# Abre um cursor ou Query.
    
    while EMAIL == 'on':

        email = input(Fore.GREEN +'\nDigite o seu e-mail de recuperação:\n')

        cursor.execute("SELECT email FROM usuarios where email = '{}'".format(email))# Verifica se o e-mail está cadastrado.

        email_bd = cursor.fetchone()# Armazena a verificação.

        if  email_bd is not None and email == email_bd[0]:# Se o e-mail já estiver cadastrado.

            system('cls')

            print('\nOk',email,'está cadastrado.\n')

            EMAIL = 'off'
            USUARIO = 'on'
        
        else:
            system('cls')
            print(Fore.RED +'\n O e-mail não foi encontrado, digite novamente.')
        
        while USUARIO == 'on':

            usuario = input(Fore.GREEN +'Agora digite o seu nome de usuário:\n')

            cursor.execute("SELECT usuario FROM usuarios where email = '{}'".format(email))# Verifica se o usuario confere com o email.

            usuario_bd = cursor.fetchone()# Armazena a verificação.

            if  usuario_bd is not None and usuario == usuario_bd[0]:# Se o usuário estiver cadastrado.

                system('cls')

                print('Usuário Ok\n')
                print('Email Ok\n')

                USUARIO = 'off'

                cursor.close() # Encerra o cursor pois não vai ser mais usado aqui.
                conn.close() # Fecha a conexão com o banco de dados.

                command = codigo_email(usuario,email)
            
            else:
                system('cls')
                print(Fore.RED +'\nUsuário incorreto, tente novamente\n')

def codigo_email(usuario,emailrec):# Recebe o e-mail de recuperação e gera o código.
    
    import random

    COD = 'on'

    codigo = random.randint(000000,900000)# Código gerado aleátoriamente de 6 digitos.

    command = enviando_email(codigo,emailrec)# Chama a função para enviar o código, passando o código e o email.

    print(Fore.YELLOW + usuario,'\nVerifique o seu E-mail foi enviado um código de recuperação.\n')

    while COD == 'on':

        codigo_digitado = int(input(Fore.GREEN + 'Digite o código de recuperação:\n'))

        if codigo == codigo_digitado :
            system('cls')
            print('\nCódigo Ok')
            COD = 'off'
            R ='on'
            command = verificador_senha(R,emailrec)

        else:
            system('cls')
            print(Fore.RED +'\nCódigo incorreto!\n')

def enviando_email(codigo,emailrec):# Código para enviar e-mail do google peguei do hastagtreinamentos.
    import smtplib
    import email.message
 
    corpo_email = f"""
    <p>Seu código de recuperação é: {codigo}</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Código de Recuperação"
    msg['From'] = 'ueslenzx@gmail.com'
    msg['To'] = emailrec
    password = 'uoklotofdfovdiyl' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

print('\n* - Sistema de Login e Cadastro - *\n')
print(' Desenvolvido por Ueslen Camargo.')
input('\n  Pressione enter para iniciar:\n')
system('cls')

command = menu_opcao()