from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <html>
    <head>
        <title>Aplicativo Alvo</title>
    </head>
    <body>
        <h1>Alterar Senha</h1>
        <form id="senhaForm" action="/alterar-senha" method="POST">
            <input type="password" name="novaSenha" placeholder="Nova Senha">
            <input type="submit" value="Alterar Senha">
        </form>
        {% if mensagem %}
        <p>{{ mensagem }}</p>
        {% endif %}
    </body>
    </html>
    """)

@app.route('/alterar-senha', methods=['POST'])
def alterar_senha():
    nova_senha = request.form.get('novaSenha')
    # Processando a nova senha
    print(f"Senha alterada para: {nova_senha}")  # Mostra a senha alterada no terminal
    mensagem = "Senha alterada com sucesso!"
    return render_template_string("""
    <html>
    <head>
        <title>Aplicativo Alvo</title>
    </head>
    <body>
        <h1>Alterar Senha</h1>
        <form id="senhaForm" action="/alterar-senha" method="POST">
            <input type="password" name="novaSenha" placeholder="Nova Senha">
            <input type="submit" value="Alterar Senha">
        </form>
        <p>{{ mensagem }}</p>
    </body>
    </html>
    """, mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
