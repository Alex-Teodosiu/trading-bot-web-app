from flask import render_template, request, redirect, url_for

def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if email and password and password == confirm_password:
            print(f'Request for register page received with email={email}')
            # Here you can add logic to save the user to a database
            return redirect(url_for('register_trading_account'))
        else:
            print('Request for register page received with invalid data')
            return render_template('register.html', error='Please provide valid data and ensure passwords match.')

    return render_template('register.html')
