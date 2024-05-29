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
    last_x_days = request.args.get('last_x_days', 30)

    url = current_app.config['AUTH_SERVER_URL'] + f"/market-data/stock_historical_market_data?symbol={symbol}&last_x_days={last_x_days}"

    response = requests.get(url)

    print(response.json())

    if response.status_code == 200:
        data = eval(response.json())
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Failed to save algorithm run'}), response.status_code


    # Mock data, replace with actual data fetching logic
    data_string = '[{"open":169.058,"high":169.55,"low":165.21,"close":166.15,"volume":45610024.0,"trade_count":520320.0,"vwap":167.157473},{"open":165.612,"high":168.1,"low":162.6,"close":162.78,"volume":33562861.0,"trade_count":393267.0,"vwap":164.538064},{"open":164.3,"high":167.12,"low":163.09,"close":163.86,"volume":33493151.0,"trade_count":406392.0,"vwap":164.848742},{"open":164.785,"high":166.73,"low":163.89,"close":166.62,"volume":24294549.0,"trade_count":297229.0,"vwap":165.748564},{"open":167.56,"high":167.96,"low":163.05,"close":167.24,"volume":34662432.0,"trade_count":429648.0,"vwap":165.93122},{"open":167.46,"high":168.14,"low":166.03,"close":168.1,"volume":21871283.0,"trade_count":312884.0,"vwap":167.265982},{"open":168.5,"high":171.76,"low":168.39,"close":171.25,"volume":28039696.0,"trade_count":356112.0,"vwap":170.708381},{"open":169.0,"high":170.15,"low":168.735,"close":169.38,"volume":19586146.0,"trade_count":240078.0,"vwap":169.542427},{"open":169.39,"high":170.69,"low":168.18,"close":169.96,"volume":15346700.0,"trade_count":232396.0,"vwap":169.280184},{"open":168.025,"high":169.85,"low":166.19,"close":168.65,"volume":29799931.0,"trade_count":397942.0,"vwap":168.227995},{"open":164.26,"high":169.28,"low":164.0,"close":169.14,"volume":31327602.0,"trade_count":423075.0,"vwap":166.900203},{"open":169.77,"high":171.25,"low":168.8,"close":170.34,"volume":25127138.0,"trade_count":322375.0,"vwap":170.112659},{"open":170.63,"high":172.65,"low":170.51,"close":172.51,"volume":26948370.0,"trade_count":340477.0,"vwap":171.912991},{"open":173.29,"high":175.115,"low":172.69,"close":174.18,"volume":27867947.0,"trade_count":319821.0,"vwap":174.15802},{"open":174.18,"high":176.265,"low":173.69,"close":176.06,"volume":24504643.0,"trade_count":277996.0,"vwap":175.68883},{"open":176.192,"high":178.77,"low":176.08,"close":176.92,"volume":22554400.0,"trade_count":283641.0,"vwap":177.160309},{"open":176.9,"high":178.15,"low":175.81,"close":177.85,"volume":16806769.0,"trade_count":232102.0,"vwap":177.48868},{"open":176.644,"high":177.15,"low":175.21,"close":176.38,"volume":17880042.0,"trade_count":257741.0,"vwap":176.0566},{"open":177.07,"high":178.25,"low":172.95,"close":173.55,"volume":21024935.0,"trade_count":280336.0,"vwap":174.685157},{"open":174.98,"high":175.77,"low":173.65,"close":174.99,"volume":16579438.0,"trade_count":235035.0,"vwap":175.000243}]'

    data = eval(data_string)  # Convert string to list of dictionaries (use with caution, eval can be dangerous with untrusted input)
    return jsonify(data)