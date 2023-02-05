from flask import Flask, render_template

app = Flask(__name__, static_folder="css")

@app.route("/userpage")
def userpage():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")



if __name__== "__main__":
    app.run(debug=True)