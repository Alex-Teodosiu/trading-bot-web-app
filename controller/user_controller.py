from flask import render_template, request, redirect, url_for, current_app, flash
import requests

def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if email and password and password == confirm_password:
            payload = {'email': email, 'password': password}
            print(f"Payload: {payload}")
            headers = {'Content-Type': 'application/json'}
            try:
                auth_server_url = current_app.config['AUTH_SERVER_URL'] + '/users/signup'
                response = requests.post(auth_server_url, json=payload, headers=headers)
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Text: {response.text}")
                response.raise_for_status()  # Raise an exception for HTTP errors

                # If the response is a string (JWT token), consider it as success
                #change the response.text to response.json()['message'] to get the error message
                if isinstance(response.text, str):
                    flash('User registered successfully. Please log in.', 'success')
                    return redirect(url_for('login'))
                else:
                    response_data = response.json()
                    error_message = response_data.get('message', 'An error occurred during registration.')
                    return render_template('register.html', error=error_message)
            except requests.exceptions.RequestException as e:
                # Attempt to extract the error message from the response, if available
                error_message = 'An error occurred while processing your request.'
                try:
                    error_message = response.json().get('message', error_message)
                except Exception:
                    print(f"An error occurred: {e}")
                return render_template('register.html', error=error_message)
        else:
            return render_template('register.html', error='Please fill out all fields correctly.')
    return render_template('register.html')
