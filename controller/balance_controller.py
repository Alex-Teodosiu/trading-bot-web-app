import requests
from flask import jsonify, current_app, render_template, session

def balance_growth():
    url = "https://paper-api.alpaca.markets/v2/account/portfolio/history"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": session.get('api_key'),
        "APCA-API-SECRET-KEY": session.get('api_secret')
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return jsonify(data)


def view_balance_growth_page():
    if not session.get('user_id'):
        return render_template('login.html')
    url = "https://paper-api.alpaca.markets/v2/account/portfolio/history"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": session.get('api_key'),
        "APCA-API-SECRET-KEY": session.get('api_secret')
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    return render_template('pages/view_balance_growth.html', balance_growth=data)