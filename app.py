from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "<h1>Welcome to My Website</h1>"

@app.route("/about")
def about():
    return "<h2>About Page</h2>"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)
