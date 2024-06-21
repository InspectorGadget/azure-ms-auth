import identity
import identity.web
import requests

from flask import Flask, session, redirect, request
from flask_cors import CORS
from flask_session import Session
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

auth = identity.web.Auth(
    session=session,
    authority=Config.AUTHORITY,
    client_id=Config.CLIENT_ID,
    client_credential=Config.CLIENT_SECRET
)

@app.route('/')
def index():
    response = auth.log_in(
        scopes=Config.SCOPE,
        redirect_uri="http://localhost:8000/token"
    )
    return redirect(response.get('auth_uri'))

@app.route('/token')
def validate():
    result = auth.complete_log_in(request.args)
    if 'error' in result:
        return 'An error has occurred', 500
    
    token = auth.get_token_for_user(Config.SCOPE)
    if 'error' in token:
        return 'An error has occurred', 500

    api_result = requests.get(
         'https://graph.microsoft.com/v1.0/me',                        
         headers={'Authorization': 'Bearer ' + token.get('access_token')},
         timeout=30                                                       
    ).json()

    return api_result

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000
    )
