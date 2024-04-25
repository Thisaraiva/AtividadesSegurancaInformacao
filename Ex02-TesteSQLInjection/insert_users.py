import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="moninha",
    database="seginf"
)

cursor = conn.cursor()

# Inserir dados de exemplo na tabela users
sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
users = [
    ("user1", "password1"),
    ("user2", "password2"),
    ("user3", "password3"),
]

cursor.executemany(sql, users)

conn.commit()
conn.close()

print("Dados inseridos com sucesso!")
