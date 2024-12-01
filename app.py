from flask import Flask, jsonify, request

app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "Service is running"}), 200

# Home endpoint
@app.route('/', methods=['GET'])
def home():
    return 'Hello, Flask World!', 200

# Add numbers endpoint
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Please provide 'a' and 'b' in JSON format"}), 400
    result = data['a'] + data['b']
    return jsonify({"result": result}), 200

# Subtract numbers endpoint
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Please provide 'a' and 'b' in JSON format"}), 400
    result = data['a'] - data['b']
    return jsonify({"result": result}), 200

# Get user info endpoint
@app.route('/user/<username>', methods=['GET'])
def user_info(username):
    return jsonify({"user": username, "message": f"Welcome, {username}!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
