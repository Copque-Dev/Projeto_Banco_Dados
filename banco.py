import sqlite3

def inicializar_banco():
    # Conecta ao banco de dados (se nao existir, ele cria o arquivo .db sozinho)
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    # Cria a tabela de usuarios se ela ainda nao existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    
    conexao.commit()
    conexao.close()

def cadastrar_usuario():
    print("\n--- Cadastro no Banco de Dados ---")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    
    try:
        conexao = sqlite3.connect('sistema.db')
        cursor = conexao.cursor()
        
        # Insere os dados na tabela usando parametros seguros
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        
        conexao.commit()
        conexao.close()
        print(f"Sucesso! Usuário {nome} cadastrado no banco.")
        
    except sqlite3.IntegrityError:
        print("Erro: Esse e-mail já está cadastrado no banco de dados.")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def listar_usuarios():
    print("\n--- Usuários Cadastrados ---")
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id, nome, email FROM usuarios")
    resultados = cursor.fetchall()
    
    conexao.close()
    
    if not resultados:
        print("Nenhum usuário cadastrado ainda.")
        return

    for linha in resultados:
        print(f"ID: {linha[0]} | Nome: {linha[1]} | E-mail: {linha[2]}")

def menu():
    inicializar_banco()
    
    while True:
        print("\n=== MENU BANCO DE DADOS ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, digite 1, 2 ou 3.")

if __name__ == "__main__":
    menu()