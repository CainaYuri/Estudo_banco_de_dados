from conexao_posr import conn 

cursor_obj = conn.cursor()

cursor_obj.execute("SELECT * FROM filmes")

result = cursor_obj.fetchall()

print(result)
