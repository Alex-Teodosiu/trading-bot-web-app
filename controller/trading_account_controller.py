from flask import render_template, request, flash, current_app, session
import requests

def register_trading_account():
    if not session.get('user_id'):
        return render_template('login.html')
    # Check if API key is already in session
    api_key_in_session = session.get('api_key')

    if request.method == 'POST':
        api_key = request.form.get('api_key')
        api_secret = request.form.get('api_secret')
        user_id = session.get('user_id')

        validation_url = current_app.config['AUTH_SERVER_URL'] + '/trading-accounts/validateaccount'
        params = {
            'user_id': user_id,
            'api_key': api_key,
            'secret': api_secret
        }

        try:
            response = requests.post(validation_url, params=params)
            response.raise_for_status()
            result = response.json()
            print(f"Validation Result: {result}")

            if result.get('id') and result.get('api_key') and result.get('api_secret') and result.get('account_number'):
                flash('Trading account validated successfully. You can now use the rest of the web app functionality!', 'success')
                session.update({'api_key': api_key, 'api_secret': api_secret})
                api_key_in_session = api_key  # Update the variable to reflect the new API key in session
            else:
                flash('Trading account validation failed.', 'danger')

        except requests.exceptions.RequestException as e:
            flash(f'An error occurred: {e}', 'danger')

    return render_template('pages/register_trading_account.html', api_key=api_key_in_session)


def get_trading_account_by_user_id(user_id):
    trading_account_url = current_app.config['AUTH_SERVER_URL'] + '/trading-accounts/get-account-by-user-id'
    params = {'user_id': user_id}
    trading_account_response = requests.get(trading_account_url, params=params)
    trading_account_response.raise_for_status()

    trading_account_data = trading_account_response.json()

    try:
        if isinstance(trading_account_data, dict) and trading_account_data.get('id') and trading_account_data.get('api_key') and trading_account_data.get('api_secret') and trading_account_data.get('account_number'):
            return trading_account_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None