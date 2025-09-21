from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management

@app.route("/")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    username = session["username"]
    account_details = "Balance: $245.67 | Premium Member"
    return render_template("index.html", username=username, account_details=account_details)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # In a real app you'd validate login here
        session["username"] = request.form["username"]
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
