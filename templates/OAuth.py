

#Add and configure the authlib OAuth component.
from flask import Flask, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth
import os
 
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure random key in production
oauth = OAuth(app)
oauth.init_app(app)

oauth.register(
  name='oidc',
  authority='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_1NJkDK1Rr',
  client_id='6vtiaq5jkuv3olp52m7v58sfr2',
  client_secret='<client secret>',
  server_metadata_url='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_1NJkDK1Rr/.well-known/openid-configuration',
  client_kwargs={'scope': 'phone openid email'}
)

#Add a home page with links to login and logout routes.
@app.route("/")
def index():
    user = session.get('user')
    if user:
        return  f'Hello, {user["email"]}. <a href="/logout">Logout</a>'
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    # Alternate option to redirect to /authorize
    # redirect_uri = url_for('authorize', _external=True)
    # return oauth.oidc.authorize_redirect(redirect_uri)
    return oauth.oidc.authorize_redirect('https://d84l1y8p4kdic.cloudfront.net')

#The OAuth module collects the access token and retrieves user data from the Amazon Cognito userInfo endpoint. Configure an authorize route to handle the access token and user data after authentication.
@app.route('/authorize')
def authorize():
    token = oauth.oidc.authorize_access_token()
    user = token['userinfo']
    session['user'] = user
    return redirect(url_for('index'))

#Configure a logout route that erases user session data.

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
