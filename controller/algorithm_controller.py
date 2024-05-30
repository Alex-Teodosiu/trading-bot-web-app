from flask import Blueprint, request, jsonify, session, render_template, current_app
import requests

algorithm_bp = Blueprint('algorithm_bp', __name__)

def select_algorithm_page():
    if not session.get('user_id'):
        return render_template('login.html')
    return render_template('pages/select_algorithm.html')


@algorithm_bp.route('/algorithm/save-algorithm-run', methods=['POST'])
def save_algorithm_run():
    user_id = session.get('user_id')
    data = request.json
    symbol = data.get('symbol')
    algorithm_name = data.get('algorithm_name')
    time_stamp = data.get('time_stamp')

    if not user_id:
        return jsonify({'error': 'User not authenticated'}), 401

    url = current_app.config['AUTH_SERVER_URL'] + '/algorithm/save-algorithm-run'
    payload = {
        "user_id": user_id,
        "symbol": symbol,
        "algorithm_name": algorithm_name,
        "time_stamp": time_stamp
    }
    print(f"Payload: {payload}")

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to save algorithm run'}), response.status_code

    

@algorithm_bp.route('/algorithm/load-running-algorithms', methods=['GET'])
def load_running_algorithms():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not authenticated'}), 401
    
    url = current_app.config['AUTH_SERVER_URL'] + '/algorithm/get-all-algorithms-by-user'
    payload = {
        "user_id": user_id
    }

    response = requests.get(url, json=payload)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch running algorithms'}), response.status_code

    response_data = response.json()

    if not isinstance(response_data, list):
        return jsonify({'error': 'Unexpected response format from server'}), 500

    formatted_algorithms = [
        {
            "algorithm": algo.get('algorithm_name'),
            "symbol": algo.get('symbol'),
            "timestamp": algo.get('time_stamp')
        }
        for algo in response_data
    ]

    if not formatted_algorithms:
        return jsonify({"running_algorithms": []}), 200

    return jsonify({"running_algorithms": formatted_algorithms}), 200



@algorithm_bp.route('/algorithm/stop-algorithm', methods=['DELETE'])
def stop_algorithm():
    data = request.json
    user_id = data.get('user_id')
    symbol = data.get('symbol')
    algorithm_name = data.get('algorithm_name')

    if not user_id:
        return jsonify({'error': 'User not authenticated'}), 401

    url = current_app.config['AUTH_SERVER_URL'] + '/algorithm/stop-algorithm'
    payload = {
        "user_id": user_id,
        "symbol": symbol,
        "algorithm_name": algorithm_name
    }

    response = requests.delete(url, json=payload)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to stop algorithm'}), response.status_code
