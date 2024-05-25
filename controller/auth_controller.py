from flask import render_template, request, redirect, url_for, session, current_app
import requests

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email and password:
            payload = {'email': email, 'password': password}
            print(f"Payload: {payload}")
            headers = {'Content-Type': 'application/json'}
            try:
                auth_server_url = current_app.config['AUTH_SERVER_URL'] + '/users/signin'
                response = requests.post(auth_server_url, json=payload, headers=headers)
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Text: {response.text}")
                response.raise_for_status()  # Raise an exception for HTTP errors
                response_data = response.json()
                if response_data.get('message') == 'Signed in successfully.':
                    session['user_id'] = response_data.get('user_id')
                    return redirect(url_for('register_trading_account'))
                else:
                    return render_template('login.html', error=response_data.get('error', 'Invalid email or password.'))
            except requests.exceptions.RequestException as e:
                # Attempt to extract the error message from the response, if available
                error_message = 'An error occurred while processing your request.'
                try:
                    error_message = response.json().get('error', error_message)
                except Exception:
                    print(f"An error occurred: {e}")
                return render_template('login.html', error=error_message)
        else:
            return render_template('login.html', error='Please provide both email and password.')

    return render_template('login.html')
