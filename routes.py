import os
from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from app import app

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')
    if name:
        print('Request for hello page received with name=%s' % name)
        return render_template('hello.html', name=name)
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if email and password and password == confirm_password:
            print(f'Request for register page received with email={email}')
            # Here you can add logic to save the user to a database
            return redirect(url_for('index'))
        else:
            print('Request for register page received with invalid data')
            # Render the form again with an error message
            return render_template('register.html', error='Please provide valid data and ensure passwords match.')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email and password:
            print(f'Request for login page received with email={email}')
            # Here you can add logic to check the user's credentials
            return redirect(url_for('index'))
        else:
            print('Request for login page received with invalid data')
            # Render the form again with an error message
            return render_template('login.html', error='Please provide valid credentials.')

    return render_template('login.html')
