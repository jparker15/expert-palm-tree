from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Lorem Ipsum API"

if __name__ == "__main":
    app.run(debug=True)