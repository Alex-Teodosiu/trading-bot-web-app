from flask import Blueprint, request, jsonify, render_template, session, current_app
import requests
import re

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/view_profile', methods=['GET'])
def profile_page():
    if not session.get('user_id'):
        return render_template('login.html')
    if get_email() is not None:
        email = get_email()
    else:
        email = None

    try:
        return render_template('pages/view_profile.html', email=email)
    except:
        return jsonify({'error': 'Failed to fetch email'}), 500

def get_email():
    user_id = session.get('user_id')
    if not user_id:
        return None

    url = current_app.config['AUTH_SERVER_URL'] + f'/users/get-email-by-id/{user_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()

        email = response.text.replace('"', '')
        return email
    except requests.RequestException as e:
        print(f"Error fetching email: {e}")
        return None

@profile_bp.route('/profile/update', methods=['PUT'])
def update_profile():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    print(session.get('user_id'))

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400
    
    url = current_app.config['AUTH_SERVER_URL'] + '/users/updateuser'
    payload = {
        'email': email,
        'password': password,
        'id': session.get('user_id')
    }

    try:
        response = requests.put(url, json=payload)
        response.raise_for_status()
        return jsonify({'message': 'Password updated successfully.'}), 200
    except requests.RequestException as e:
        return jsonify({'error': 'Failed to update profile', 'details': str(e)}), response.status_code
    

@profile_bp.route('/profile/delete', methods=['DELETE'])
def delete_account():
    data = request.json
    email = data.get('email')
    # password = data.get('password')

    if not email:
        return jsonify({'error': 'Email and password are required'}), 400

    url = current_app.config['AUTH_SERVER_URL'] + '/users/deleteuser'
    payload = {
        'email': email,
        'id': session.get('user_id')
    }

    try:
        response = requests.delete(url, json=payload)
        response.raise_for_status()
        session.clear()
        return jsonify({'message': 'User deleted successfully.'}), 200
    except requests.RequestException as e:
        return jsonify({'error': 'Failed to delete account', 'details': str(e)}), response.status_code
