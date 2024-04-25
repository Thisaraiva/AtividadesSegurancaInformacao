from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h2>Formulário de Login</h2>
    <form action="/login" method="post">
        Nome de Usuário: <input type="text" name="username"><br>
        Senha: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="moninha",
        database="seginf"
    )

    # injection sql => ' OR '1'='1

    cursor = conn.cursor()

    
    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))
    users = cursor.fetchall()

    conn.close()

    if users:
        return f"Usuários encontrados: {users}"
    else:
        return "0 resultados"

if __name__ == '__main__':
    app.run(debug=True)


#SQL Injection - ' OR '1'='1