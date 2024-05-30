from flask import Flask, render_template, jsonify, request, Blueprint, current_app, session
import requests
from datetime import datetime, timedelta
import json

stock_bp = Blueprint('stock_bp', __name__)

@stock_bp.route('/stocks')
def view_stocks():
    if not session.get('user_id'):
        return render_template('login.html')
    return render_template('pages/view_stocks.html')

@stock_bp.route('/stock_historical_market_data', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol')
    last_x_days = request.args.get('last_x_days')

    url = current_app.config['AUTH_SERVER_URL'] + f"/market-data/stock_historical_market_data?symbol={symbol}&last_x_days={last_x_days}"

    response = requests.get(url)

    print(response.json())

    if response.status_code == 200:
        data = eval(response.json())
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Failed to save algorithm run'}), response.status_code

