from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__, static_url_path="/static/styles.css")



@app.route("/me")
def hello_world():
    return """
    <p>HELLO, WORLD</p>
    <a href="/me">click me</a>
"""

def randomBit():
    return "<a href='/'>Back</a>"

@app.route("/")
def indexHTML():
    return render_template("index.html")

@app.route("/meo")
def me():
    lol = hello_world()
    return f"HI, IAM ME<br>{randomBit()}{indexHTML()}"
