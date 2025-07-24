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
