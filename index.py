# Imports
# 3rd Party
from flask import Flask, render_template, redirect, url_for, request, session
from authlib.integrations.flask_client import OAuth
import os

# Library
from AWS_services.RDS.query_files import query_files
from AWS_services.RDS.add_file_metadata import add_file_metadata
from Library.Utilities import allowed_file

app = Flask(__name__)

# FIle Storage
UPLOAD_FOLDER = 'uploads'  # Specify the folder where files will be stored
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}  # Specify allowed file types
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit to 16MB

# AWS Cognito OAuth Config
oauth = OAuth(app)
oauth.init_app(app)
app.secret_key = os.urandom(24)  # Use a secure random key in production


oauth.register(
  name='oidc',
  authority='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_2xD8x1SQF',
  client_id='1tbjqsnjuso91ot481uabf78va',
  client_secret='<client secret>',
  server_metadata_url='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_2xD8x1SQF/.well-known/openid-configuration',
  client_kwargs={'scope': 'email openid phone'}
)

@app.route("/")
def index():
    user = session.get('user')
    if user:
        return render_template('Principal.html')
    else:
        # return render_template('Login.html')
        return render_template('Principal.html')

@app.route("/buscar")
def buscar():
    return render_template('Buscador.html')

@app.route("/agregar")
def agregar():
    return render_template('Agregar.html')

@app.route("/principal")
def principal():
        return  render_template('Principal.html')


@app.route('/login')
def login():
    # Alternate option to redirect to /authorize
     redirect_uri = url_for('authorize', _external=True)
    # Add `ui_locales=es` to the redirect URL to specify Spanish
     authorization_url = oauth.oidc.authorize_redirect(redirect_uri, ui_locales='es')
     return oauth.oidc.authorize_redirect('https://d84l1y8p4kdic.cloudfront.net', ui_locales='es')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/authorize')
def authorize():
    token = oauth.oidc.authorize_access_token()
    user = token['userinfo']
    session['user'] = user
    return redirect(url_for('index'))

@app.route("/register")
def register():
   

    # TODO Manage the Call for Login Validation to AWS Cognito here

    # Call a AWS Cognito and Pass Params
    result = None

    # Return a response (could be a new template or a message)
    return oauth.oidc.authorize_redirect('https://us-east-11njkdk1rr.auth.us-east-1.amazoncognito.com/signup?client_id=6vtiaq5jkuv3olp52m7v58sfr2&nonce=nh4mVYmSv0737q4AiFTz&redirect_uri=https%3A%2F%2Fd84l1y8p4kdic.cloudfront.net&response_type=code&scope=phone+openid+email&state=NJYIlHk6lKpt5wkm6mf3u6G0fyiNku')

@app.route("/account_recovery")
def account_recovery():
    # TODO Manage the Call for Login Validation to AWS Cognito here

    # Call a AWS Cognito and Pass Params
    result = None

    # Return a response (could be a new template or a message)
    return f"Form submitted! Processed input: {result}"


@app.route("/search_results", methods=['POST'])
def search_results():
    # Extract Parameters to search with
    selections = {}

    # Loop through all form fields (keys)
    for key, value in request.form.items():
        selections[key] = value

    # Call underlying function
    sql_results = query_files(selections)

    # Transform Results to pass as Parameters for HTML Generation
    results = []

    for result in sql_results:
        file_name = os.path.basename(result['file_key'])
        url_result = url_for('static', filename=f'uploads/{file_name}')
        results.append({'nombre': file_name, "url": url_result})

    # Return the Template to Render and Parameters for Dynamic HTML
    return render_template('ResultadosBusqueda.html', resultados=results)

@app.route("/upload", methods=['POST'])
def add_homework():
    # TODO Can most likely greatly improve code by simply returning one "render_template at the end" and just storing a string for type of message to display.
    if request.method == 'POST':
        # Extract Parameters to search with
        selections = {}

        # Loop through all form fields (keys)
        for key, value in request.form.items():
            selections[key] = value

        file = request.files['file']

        # If no file is selected
        if file.filename == '':
            return render_template('Agregar_Result_Screen.html', result='Archivo no tiene nombre valido.')

        if file and allowed_file(file.filename, app):
            # Secure the filename (to avoid malicious filenames)
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # TODO Improve error handling here, by putting all this in a generic try - except Clause
            # Save the file
            file.save(filepath)

            user_id = 'WIP'  # TODO ADD IN AWS COGNITO ID FOR WHO IS UPLOADING HERE

            # Store Metadata
            result = add_file_metadata((selections['materia'], selections['grado'], selections['destreza'], selections['nivel'], filepath, user_id))

            if result != 'success':
                return render_template('Agregar_Result_Screen.html', result=f'Internal Error when adding File metadata to RDS, report to admin.')

            return render_template('Agregar_Result_Screen.html', result=f'Archivo {filename} subido correctamente.')

        return render_template('Agregar_Result_Screen.html', result='Tipo de Archivo subido no permitido.')

    result = 'Method Not Post, not sure how you got here, should not happen please report to admin.'

    # Redirect to Result Screen
    return render_template('Agregar_Result_Screen.html', result=result)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='localhost', port=5001)