from flask import Flask
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Make sure to set a secret key
app.config['AUTH_SERVER_URL'] = os.getenv('AUTH_SERVER_URL')

# Register routes
from routes import *

if __name__ == '__main__':
    app.run()
