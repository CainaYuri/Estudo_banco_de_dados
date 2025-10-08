from conexao_posr import conn

cursor_obj = conn.cursor()

filmes = [
    ('Um sonho de amor', 2023, 5.7),
    ('Amor de um sonho', 2000, 9.0),
    ('Terror do kamasutra', 1985, 9.7)
]

for filme in filmes:
    cursor_obj.execute(
        """
            INSERT INTO filmes(nome, ano, nota)
            VALUES (%s, %s, %s)
        """, filme
    )

conn.commit()
print("Dados inseridos com sucesso")
conn.close()

