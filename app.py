from flask import Flask, render_template, redirect, request, session

USER = "naamis"
PWD = "kakka12"
app = Flask(__name__, static_folder="css")
app.secret_key = "4815162342"

@app.route("/userpage")
def userpage():
    if session.get("username"):
        return render_template("index.html")
    return redirect("/")
    

@app.route("/about")
def about():
    if session.get("username"):
        return render_template("about.html")
    return redirect("/")

@app.route("/portfolio")
def portfolio():
    if session.get("username"):
        return render_template("portfolio.html")
    return redirect("/")

@app.route("/")
def landing():
    if session.get("username"):
        return redirect("/userpage")
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if USER == username.lower() and PWD == password:
        session["username"] = username
        return redirect("/userpage")
    return redirect("/")

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/")
    

if __name__== "__main__":
    app.run(debug=True)