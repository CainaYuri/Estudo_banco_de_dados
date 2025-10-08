import sqlite3

#conexao com bando de dados 
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

#Inserir dados

cursor.execute(
    """
        INSERT INTO filmes(nome, ano, note)
        VALUES ('Super Mario Bros', 2022, 9.5),
         ('Matrix', 1999, 10), ('Bacural', 2022, 7.0)
        
        

    """
)

conexao.commit()
conexao.close()
print("Dados inseridos na tabela")

