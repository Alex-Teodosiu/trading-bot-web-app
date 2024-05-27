from flask import Flask
import os
from controller.algorithm_controller import algorithm_bp
from controller.profile_controller import profile_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Make sure to set a secret key
app.config['AUTH_SERVER_URL'] = os.getenv('AUTH_SERVER_URL')

# Register routes
from routes import *


app.register_blueprint(algorithm_bp)
app.register_blueprint(profile_bp)

if __name__ == '__main__':
    app.run()
