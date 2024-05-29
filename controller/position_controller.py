import requests
from flask import render_template, request, session, flash

def view_open_positions():
    if not session.get('user_id'):
        return render_template('login.html')
    user_id = session.get('user_id')
    
    if not user_id:
        flash('User not logged in.', 'danger')
        return render_template('pages/view_open_positions.html', positions=[], long_count=0, short_count=0)

    api_url = 'https://automated-trading-bot-server.azurewebsites.net/positions/get-all-open-positions'
    params = {'user_id': user_id}
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        positions = response.json()

        long_count = sum(1 for position in positions if position['side'] == 'long')
        short_count = sum(1 for position in positions if position['side'] == 'short')

        # Convert string values to float where necessary
        for position in positions:
            position['qty'] = float(position['qty'])
            position['market_value'] = float(position['market_value'])
            position['cost_basis'] = float(position['cost_basis'])
            position['unrealized_pl'] = float(position['unrealized_pl'])
            position['unrealized_plpc'] = float(position['unrealized_plpc'])
            position['current_price'] = float(position['current_price'])

    except requests.exceptions.RequestException as e:
        flash(f'An error occurred: {e}', 'danger')
        positions = []
        long_count = 0
        short_count = 0

    return render_template('pages/view_open_positions.html', positions=positions, long_count=long_count, short_count=short_count)
