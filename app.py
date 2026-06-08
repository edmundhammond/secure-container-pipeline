from flask import Flask, request
import os
import werkzeug

app = Flask(__name__)


SECRET_API_KEY = os.environ.get("SECURE_API_KEY", "default_fallback_value")

@app.route('/')
def home():
    return "<h1>Welcome to the Secure Web App Demo!</h1>"

@app.route('/run')
def run_command():
    
    user_input = request.args.get('cmd', '')
    
    
    safe_output = werkzeug.utils.escape(user_input)
    
    return f"<h1>Executing Safe Output Validation:</h1><pre>{safe_output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)