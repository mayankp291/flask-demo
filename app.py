from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask App"

@app.route("/<name>")
def msg(name):
    return f"Hi {name}"
    
if __name__ == "__main__":
    app.run(debug=True)
