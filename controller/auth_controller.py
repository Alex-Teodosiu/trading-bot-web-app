from flask import render_template, request, redirect, url_for, session, current_app
import requests
import controller.trading_account_controller as trading_account_controller

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(f"Email: {email}, Password: {password}")

        if email and password:
            payload = {'email': email, 'password': password}
            headers = {'Content-Type': 'application/json'}
            try:
                auth_server_url = current_app.config['AUTH_SERVER_URL'] + '/users/signin'
                response = requests.post(auth_server_url, json=payload, headers=headers)
                response.raise_for_status()  
                response_data = response.json()
                print(response_data)
                print(response_data.get('message'))
                if response_data.get('message') == 'Signed in successfully.':
                    print('User signed in successfully.')
                    print(response_data.get('user_id'))
                    session['user_id'] = response_data.get('user_id')

                    # Check if the user has a trading account
                    try:
                        trading_account_data = trading_account_controller.get_trading_account_by_user_id(session.get('user_id'))
                        print(trading_account_data)
                    except requests.exceptions.RequestException as e:
                        print(f"An error occurred: {e}")
                        return render_template('login.html', error='An error occurred while processing your request.')
                    if trading_account_data is not None and trading_account_data.get('api_key') and trading_account_data.get('api_secret'):
                        session['api_key'] = trading_account_data.get('api_key')
                        session['api_secret'] = trading_account_data.get('api_secret')
                        return redirect(url_for('register_trading_account'))
                    else:
                        return redirect(url_for('register_trading_account'))

                else:
                    return render_template('login.html', error=response_data.get('error', 'Invalid email or password.'))
            except requests.exceptions.RequestException as e:
                error_message = 'An error occurred while processing your request.'
                try:
                    error_message = response.json().get('error', error_message)
                except Exception:
                    print(f"An error occurred: {e}")
                return render_template('login.html', error=error_message)
        else:
            return render_template('login.html', error='Please provide both email and password.')

    return render_template('login.html')