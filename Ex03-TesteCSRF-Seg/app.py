from flask import Flask, request, render_template, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Chave secreta para a sessão

def gerar_token_csrf():
    if 'csrf_token' not in session:
        session['csrf_token'] = os.urandom(24).hex()
    return session['csrf_token']

@app.route('/')
def index():
    csrf_token = gerar_token_csrf()
    return render_template("index.html", csrf_token=csrf_token)

@app.route('/alterar-senha', methods=['POST'])
def alterar_senha():
    nova_senha = request.form.get('novaSenha')
    token_csrf = request.form.get('csrf_token')

    # Verificar o token CSRF
    if token_csrf != session.pop('csrf_token', None):
        return "Token CSRF inválido", 400

    # Processando a nova senha
    print(f"Senha alterada para: {nova_senha}")  # Mostra a senha alterada no terminal
    mensagem = "Senha alterada com sucesso!"
    return render_template("index.html", mensagem=mensagem, csrf_token=gerar_token_csrf())

if __name__ == '__main__':
    app.run(debug=True)
