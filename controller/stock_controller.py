# import requests
# from flask import Blueprint, render_template, request, current_app, session


# stocks_blueprint = Blueprint('stocks', __name__)

# API_URL = current_app.config['AUTH_SERVER_URL'] + '/market-data/stock_historical_market_data'

# @stocks_blueprint.route('/view_stocks', methods=['GET'])
# def view_stocks():
#     if request.method == 'GET':
#         user_id = session.get('user_id')
#         api_key = session.get('api_key')
#         api_secret = session.get('api_secret')
#         symbols = request.args.get('symbols', 'MSFT,AAPL,NVDA').split(',')
#         days = request.args.get('days', 7)
#         stock_data = {}

#         for symbol in symbols:
#             response = requests.get(f"{API_URL}?symbol={symbol}&last_x_days={days}")
#             if response.status_code == 200:
#                 stock_data[symbol] = response.json()
#                 print(f"Stock data for {symbol}: {stock_data[symbol]}")
#             else:
#                 stock_data[symbol] = {"error": "Data not available"}

#     return render_template('view_stocks.html', stock_data=stock_data)
