from flask import render_template, request, redirect, url_for, flash

def register_trading_account():
    return render_template('pages/register_trading_account.html', signed_in=True)

def save_trading_account():
    api_key = request.form.get('api_key')
    api_secret = request.form.get('api_secret')
    
    # Save the API key and secret (this is just an example; in practice, you should save it securely)
    print(f"Received API Key: {api_key}")
    print(f"Received API Secret: {api_secret}")
    
    # Add your logic to save the API key and secret here

    flash('Trading account credentials saved successfully!', 'success')
    return redirect(url_for('register_trading_account'))
