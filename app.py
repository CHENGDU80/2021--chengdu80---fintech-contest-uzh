from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('sb-admin/index.html')
#    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    app.run()

