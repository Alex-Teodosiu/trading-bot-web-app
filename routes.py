from flask import send_from_directory, render_template, redirect, url_for, session, flash
from app import app
from controller import auth_controller, user_controller, trading_account_controller
import os

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html', signed_in=False)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    return user_controller.hello()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return user_controller.register()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return auth_controller.login()

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/register_trading_account', methods=['GET'])
def register_trading_account():
    return trading_account_controller.register_trading_account()

@app.route('/register_trading_account', methods=['POST'])
def save_trading_account():
    return trading_account_controller.save_trading_account()

@app.route('/view_stocks')
def view_stocks():
    return render_template('pages/view_stocks.html', signed_in=True)

@app.route('/select_algorithm')
def select_algorithm():
    return render_template('pages/select_algorithm.html', signed_in=True)

@app.route('/view_trade_history')
def view_trade_history():
    return render_template('pages/view_trade_history.html', signed_in=True)
