import sqlite3

#conexao
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#leitura de dados 
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())

