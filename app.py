from flask import Flask

app = Flask(__name__)

# Register routes
from routes import *

if __name__ == '__main__':
    app.run()
