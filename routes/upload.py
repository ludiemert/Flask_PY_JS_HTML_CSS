from flask import Blueprint, request, render_template
import os
from werkzeug.utils import secure_filename

upload_bp = Blueprint('upload', __name__)
#Você está usando Blueprints para modularizar o código. O Blueprint é uma forma de organizar o código, especialmente quando a aplicação cresce em tamanho. Ele permite que você crie grupos de rotas e lógicas de aplicação em arquivos separados.
#O Blueprint ajuda a manter o código mais limpo e organizado.


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'arquivo' not in request.files:
            return render_template('upload_response.html', mensagem="No file sent.")
        file = request.files['arquivo']
        if file.filename == '':
            return render_template('upload_response.html', mensagem="No file selected.")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Garante que a pasta exista
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return render_template('upload_response.html', mensagem=f"File {filename} successfully sent! 🎉🎉")

    return render_template('upload_response.html', mensagem="File type not permitted. 😣")
