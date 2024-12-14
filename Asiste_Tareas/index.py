# Imports
# 3rd Party
from flask import Flask, render_template, redirect, url_for, request, session
from authlib.integrations.flask_client import OAuth
import os
# Library
#from AWS_services.Lambda.query_files import query_files

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure random key in production
oauth = OAuth(app)
oauth.init_app(app)


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
        return render_template('Login.html')

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

if __name__ == '__main__':
    app.run(debug=True)

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

    print(selections)

    # TODO Generate the SQL for Querying the table with these selection parameters
    sql_string = 'WIP'

    # TODO Call underlying function
   # result = query_files(sql_string)
    result = None
    # TODO Manipulate Result and pass to the Search_Results_HTML

    # TODO Return the Template to Render and Parameters for Dynamic HTML
    return f"Form submitted! Processed input: {result}"

@app.route("/add_homework", methods=['POST'])
def add_homework():
    # Extract Parameters to search with
    selections = {}

    # Loop through all form fields (keys)
    for key, value in request.form.items():
        selections[key] = value

    print(selections)

    # Get uploaded file
    file = request.files.get('file')  # Retrieve the uploaded file

    # TODO Validate File such as no bigger than X megabytes and have allowed extensions

    # TODO Call underlying function to upload to S3
    # TODO Returns the Key of where/how it was stored
    # TODO Add into the RDS Table a new row with the metadata and storage key of the file
    result = None

    # TODO Manipulate Result and pass to the Homework Added HTML or something IDK yet

    # Redirect back to Main Page
    return f"Form submitted! Processed input: {result}"

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='localhost', port=5001)