from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database
users = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']
        password = request.form['password']

        for user in users.values():
            if (user['email'] == identifier or user['phone'] == identifier) and user['password'] == password:
                return f"Welcome, {user['username']}!"
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm:
            return "Passwords do not match", 400
        if email in users:
            return "Email already registered", 400

        users[email] = {
            'username': username,
            'email': email,
            'phone': phone,
            'password': password
        }
        return redirect(url_for('login'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
