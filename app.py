

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('pages/base.html')