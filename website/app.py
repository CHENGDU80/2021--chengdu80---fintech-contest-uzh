from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('sb-admin/index.html')
#    return "<h1>Hello, World!</h1>"

@app.route("/login1")
def login1():
    return render_template('sb-admin/login.html')

@app.route("/show_company")
def show_company():
    return render_template('sb-admin/show_company.html')

@app.route("/subscriptions")
def subscriptions():
    return render_template('sb-admin/subscriptions.html')


if __name__ == "__main__":
    app.run()

