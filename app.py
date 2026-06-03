from flask import Flask, request
import os

app = Flask(__name__)


SECRET_API_KEY = "AIzaSyA123456789-FakeGoogleKeyForTesting"

@app.route('/')
def home():
    return "<h1>Welcome to the Secure Web App Demo!</h1>"

@app.route('/run')
def run_command():
    
    cmd = request.args.get('cmd', '')
    
    response = os.popen(cmd).read()
    return f"<pre>{response}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)