from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <p>HELLO, WORLD</p>
    <a href="/me">click me</a>
"""

def randomBit():
    return "<a href='/'>Back</a>"

@app.route("/me")
def me():
    lol = hello_world()
    return f"HI, IAM ME<br>{randomBit()}"