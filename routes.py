from flask import send_from_directory, render_template, redirect, url_for, session, flash
from app import app
from controller import auth_controller, user_controller, trading_account_controller, position_controller
from controller import profile_controller, algorithm_controller, balance_controller, stock_controller
import os
# from controller.stock_controller import stocks_blueprint

# def initialize_routes(app):
#     app.register_blueprint(stocks_blueprint)

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html', signed_in=False)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return user_controller.register()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return auth_controller.login()

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/register_trading_account', methods=['GET', 'POST'])
def register_trading_account():
    return trading_account_controller.register_trading_account()

@app.route('/view_stocks')
def view_stocks():
    return stock_controller.view_stocks()

@app.route('/select_algorithm')
def select_algorithm():
    return algorithm_controller.select_algorithm_page()

@app.route('/view_open_positions', methods=['GET', 'POST'])
def view_open_positions():
    return position_controller.view_open_positions()

@app.route('/view_balance_growth', methods=['GET', 'POST'])
def view_balance_growth():
    return balance_controller.view_balance_growth_page()

@app.route('/view_profile')
def view_profile():
    return profile_controller.profile_page()
