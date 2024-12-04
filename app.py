from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename

from routes.upload import upload_bp  # Importa o blueprint de upload

app = Flask(__name__)

# Configuração do diretório de uploads
app.config['UPLOAD_FOLDER'] = 'uploads'

# Registrar o blueprint de upload
#app.register_blueprint(upload_bp): Registra um Blueprint. O Blueprint é uma maneira de organizar as rotas de uma aplicação Flask em módulos separados.
app.register_blueprint(upload_bp)

@app.route('/')
def home():
    return render_template('index.html')  # Renderiza o arquivo HTML

# Validação de nome (o nome não pode ser vazio e deve ter mais de 3 caracteres)
#@app.route('/processar', methods=['POST']): Esta rota é acessada quando o formulário da página index.html é enviado. Ela recebe uma requisição do tipo POST (usada quando os dados são enviados via formulário).
@app.route('/processar', methods=['POST'])
def processar():
    nome = request.form['nome']  # Obtém o valor do campo 'nome' do formulário, equest.form['nome']: Acessa o dado enviado pelo usuário no campo nome do formulário. O Flask armazena esses dados no objeto request.form.
    telefone = request.form.get('telefone')  # Telefone opcional, request.form.get('telefone') e request.form.get('email'): Usado para acessar os valores dos campos "telefone" e "email". O .get() é uma maneira segura de acessar os dados, já que retorna None caso o campo não exista.
    email = request.form.get('email')  # Email opcional

    # Verificar se o nome é válido
    if not nome or len(nome) < 3:
        return render_template('index.html', error="Name must have at least 3 characters!")

    # Aqui você pode adicionar validações para telefone e email, caso precise

    # Se a validação passar, renderiza a página de resposta
    return render_template('response.html', nome=nome, telefone=telefone, email=email)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True): Inicia o servidor Flask em modo de depuração (debug=True), o que significa que a aplicação será recarregada automaticamente quando houver mudanças no código. Ideal para desenvolvimento.