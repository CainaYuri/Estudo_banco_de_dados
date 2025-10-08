import sqlite3

#criando o banco de dados 
conexao = sqlite3.connect("titulo.db")

#cursor
cursor = conexao.cursor()

#tabela
cursor.execute(
    '''
        CREATE TABLE filmes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTERGER NOT NULL,
        note REAL NOT NULL);
        
'''
)

conexao.close()
print("Tabela criada")
