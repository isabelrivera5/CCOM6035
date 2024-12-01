# Imports
# 3rd Party
from flask import Flask, render_template, redirect, url_for, request

# Library
from AWS_services.Lambda.query_files import query_files

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('Login.html')

@app.route("/buscar")
def buscar():
    return render_template('Buscador.html')

@app.route("/agregar")
def agregar():
    return render_template('Agregar.html')

@app.route("/principal")
def principal():
    return render_template('Principal.html')

@app.route("/login", methods=['POST'])
def login():
    # Get data from the form
    email = request.form.get('input_email')
    password = request.form.get('input_password')

    # TODO Manage the Call for Login Validation to AWS Cognito here

    # Call a AWS Cognito and Pass Params
    result = None

    # Return a response (could be a new template or a message)
    return f"Form submitted! Processed input: {result}"

@app.route("/register", methods=['POST'])
def register():
    # Get data from the form
    password = request.form.get('input_user')
    email = request.form.get('input_email')
    password = request.form.get('input_password')

    # TODO Manage the Call for Login Validation to AWS Cognito here

    # Call a AWS Cognito and Pass Params
    result = None

    # Return a response (could be a new template or a message)
    return f"Form submitted! Processed input: {result}"

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
    result = query_files(sql_string)

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
    app.run(debug=True)
