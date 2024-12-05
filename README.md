## Flask_PY_JS_HTML_CSS
 - Web Integration Project with Flask, HTML, CSS, and JavaScript
 - This project integrates Flask (Python) with HTML, CSS, and JavaScript to create a functional and interactive web application. The app allows users to submit a form with personal information and upload files. The project demonstrates how to create interactive forms, process data, and use Flask for routing and dynamic templating.

---

<h4 align="center">Web - Flask_PY_JS_HTML_CSS 🚀</h4>

<div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img/01_Flask_PY_JS_HTML_CSS_app.py.png" style="width: 90%;" alt="01_Flask_PY_JS_HTML_CSS_app.py">
                <p style="margin-top: 5px;">Flask_PY_JS_HTML_CSS_app.py</p>
            </td>
            <td style="width: 50%; text-align: center;">
                <img src="img/01_Project_page_Codig.png" style="width: 90%;" alt=01_Project_page_Codig">
                <p style="margin-top: 5px;">Project_page_Codig</p>
            </td>
        </tr>
    </table>
</div>

  <br/>
  <br/>


<div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img/5_name_pag_route_proc.png" style="width: 90%;" alt="5_name_pag_route_proc">
                <p style="margin-top: 5px;">Name_pag_route_proc</p>
            </td>
            <td style="width: 50%; text-align: center;">
                <img src="img/6_pag_upload.png" style="width: 90%;" alt=6_pag_upload.">
                <p style="margin-top: 5px;">Page_upload</p>
            </td>
        </tr>
    </table>
</div>

  <br/>
  <br/>

  <div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img/02_Flask_PY_JS_HTML_CSS_app.py.png" style="width: 90%;" alt="02_Flask_PY_JS_HTML_CSS_app.py">
                <p style="margin-top: 5px;">Color_Flask_PY_JS_HTML_CSS_app.py</p>
            </td>
            <td style="width: 50%; text-align: center;">
                <img src="img/4_teste_name_erro.png" style="width: 90%;" alt=4_teste_name_erro">
                <p style="margin-top: 5px;">Teste_name_erro</p>
            </td>
        </tr>
    </table>
</div>

  <br/>
  <br/>

  <div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img/7_pag_ok_upload.png" style="width: 90%;" alt="7_pag_ok_upload">
                <p style="margin-top: 5px;">Page_ok_upload</p>
            </td>          
        </tr>
    </table>
</div>

  <br/>
  <br/>
  
---



#### Features
 - Interactive Form: Users can fill out a form with name, phone number, and email.
 - File Upload: Users can upload files with allowed types such as images and text files.
 - Data Validation: The name validation ensures it has at least 3 characters, while the file validation ensures only allowed file types are uploaded.
 - Dynamic Color Effect: JavaScript is used to change the page background color with an interactive rainbow gradient.
 - Modular Structure: The code is split into separate files using Blueprints in Flask, making the application more maintainable and organized.

----

#### Technologies Used
 - Python (Flask): Web framework used for the backend of the application.
 - JavaScript: DOM manipulation and page interactivity, including the color-changing effect.
 - HTML: Structuring and layout of the web application.
 - CSS (with Flexbox and Grids): Styling the application, including responsiveness.
 - Werkzeug: Used to ensure that file names are secure when uploading.

----


#### How to Run the Project
 #####  Prerequisites
 
 - Python 3.13 installed
 - Pip for managing dependencies

----

 ##### Install Dependencies
 1 - Clone this repository:
 
   ```bash
   git clone [https://github.com/username/repository-name] https://github.com/ludiemert/Flask_PY_JS_HTML_CSS.git

  ```

----

 2 - Navigate to the project directory:
 
  ```bash
   cd repository-name

  ```


----

 3 - Install the dependencies:
 
  ```bash
   pip install -r requirements.txt
 ```
   
----

  4 - Start the Flask server:
  
    ```bash
      python app.py    
    ```

    ----

   5 - Web 💻

     -  The server will be available at http://127.0.0.1:5000/

 ----

#### 💻 How It Works

1. Home Page (/):
On the homepage, the user can fill out a form with their name, phone number, and email. When the form is submitted, the data is processed and validated on the backend, and a response page is returned with the user's information.

2. File Upload (/upload):
The user can upload files to the server. The backend validates the file type (only specific types like .png, .jpg, .txt, etc., are allowed) and saves the file to the uploads directory.

3. Response Page:
After the form or file upload is submitted, a response page is rendered, showing whether the submission was successful or if there were errors (e.g., file not allowed or invalid name).

----

####  File Structure

 ```bash
.
├── app.py                # Main Flask file (Backend)
├── requirements.txt      # Project dependencies
├── routes/
│   ├── __init__.py       # Initializes the Blueprint for the upload route
│   └── upload.py         # File upload logic
├── templates/
│   ├── index.html        # Home page with the form
│   └── upload_response.html  # Response page for file upload
├── static/
│   ├── css/
│   │   └── style1.css    # Styling for the page
│   ├── img/
│   │   ├── logo.png      # Logo of the app
│   │   └── favicon.ico   # Icon for the page
└── uploads/              # Directory to store uploaded files

```

#### How to Contribute
 - Feel free to contribute to this project! To suggest improvements or fix issues, simply create a pull request or open an issue.

 - Fork this repository.
 - Create a branch with your changes.
 - Commit your changes.
 - Submit a pull request to the main branch.

-------

#### Portugues 🧐

### Projeto de Integração Web com Flask, HTML, CSS e JavaScript
 - Este projeto integra Flask (Python) com HTML, CSS e JavaScript para criar uma aplicação web funcional e interativa.
 - A aplicação permite que os usuários enviem um formulário com informações pessoais e realizem o upload de arquivos. O projeto demonstra como criar formulários interativos, processar dados e usar o Flask para gerenciar rotas e templates dinâmicos.

----

#### Funcionalidades
 - Formulário Interativo: O usuário pode preencher um formulário com nome, telefone e email.
 - Upload de Arquivos: O usuário pode enviar arquivos com tipos permitidos, como imagens e arquivos de texto.
 - Validação de Dados: A validação do nome garante que ele tenha pelo menos 3 caracteres, enquanto a verificação de arquivos garante que sejam tipos 
  permitidos.
 - Efeito de Cor Dinâmica: Utiliza JavaScript para alterar a cor de fundo da página, com um degradê em arco-íris interativo.
 - Estrutura Modularizada: O código é dividido em arquivos separados utilizando Blueprints no Flask, organizando melhor a aplicação e facilitando a 
   manutenção.

----

#### Tecnologias Utilizadas
 - Python (Flask): Framework web utilizado para o backend da aplicação.
 - JavaScript: Manipulação dinâmica do DOM e interatividade da página, como o efeito de troca de cores.
 - HTML: Estruturação e layout da aplicação.
 - CSS (com Flexbox e Grids): Estilização da aplicação, incluindo responsividade.
 - Werkzeug: Utilizado para garantir que os nomes de arquivos sejam seguros ao fazer o upload.

 ----
 

 #### Como Funciona
1. Página Inicial (/):
Na página inicial, o usuário pode preencher um formulário com informações como nome, telefone e email. Quando o formulário é enviado, os dados são processados e validados no backend, retornando uma resposta com as informações do usuário.

2. Upload de Arquivos (/upload):
O usuário pode enviar arquivos para o servidor. O backend valida o tipo de arquivo (permitindo apenas extensões específicas como .png, .jpg, .txt etc.) e armazena o arquivo no diretório uploads.

3. Página de Resposta:
Após o envio do formulário ou arquivo, uma página de resposta é renderizada, mostrando ao usuário se o envio foi bem-sucedido ou se houve algum erro (por exemplo, se o arquivo não for permitido ou se o nome não for válido).

----

#### Como Contribuir
 - Sinta-se à vontade para contribuir com este projeto! Para sugerir melhorias ou corrigir problemas, basta criar um pull request ou abrir uma issue.

 - Faça um fork deste repositório.
 - Crie uma branch com suas mudanças.
 - Faça um commit com suas alterações.
 - Envie um pull request para o branch main.

-----
   

- #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

#### Contact

<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
🖥️ Python Enthusiast | Computer Vision | AI Integrations <br>
📍 São Jose dos Campos – SP, Brazil

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>
