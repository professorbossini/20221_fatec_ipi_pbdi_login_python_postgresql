import psycopg

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

#definição do método: ele recebe um objeto do tipo Usuario
def existe (usuario):
    #Abre a conexão
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20221_fatec_ipi_pbdi_login",
        user="postgres",
        password="postgres"
        ) as conexao:
        #obtém um cursor
        with conexao.cursor() as cursor:
            #executa o comando
            cursor.execute('SELECT * FROM tb_usuario WHERE login=%s AND senha=%s', (f'{usuario.login}', f'{usuario.senha}'))
            #obtém o resultado
            result = cursor.fetchone()
            #verifica se o resultado é diferente de None, o
            #que indica que o usuário existe na base
            return result != None


#0- Sair
#1- Fazer login
#2- Fazer logoff

def menu():
    #texto que vai ser exibido
    texto = "0-Fechar sistema\n1-Login\n2-Logoff"
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input ("Digite seu login\n")
            senha = input ("Digite a sua senha\n")
            usuario = Usuario(login, senha)
            usuario_existe = existe(usuario)
            print ("Usuário OK" if usuario_existe else "Usuário NOK")
            if not usuario_existe:
                usuario = None

        elif op == 2:
            usuario = None
            print ("Logoff realizado com sucesso")
        
        op = int (input(texto))
    else:
        print ("Até mais")

menu()

