from flask import render_template, request, redirect, url_for
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
                response = requests.post('http://127.0.0.1:5000/users/signin', json=payload, headers=headers)
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Text: {response.text}")
                response.raise_for_status()  # Raise an exception for HTTP errors
                response_data = response.json()
                if response_data.get('message') == 'Signed in successfully.':
                    return redirect(url_for('register_trading_account'))
                else:
                    return render_template('login.html', error='Invalid email or password.')
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return render_template('login.html', error='An error occurred while processing your request.')
        else:
            return render_template('login.html', error='Please provide both email and password.')

    return render_template('login.html')
