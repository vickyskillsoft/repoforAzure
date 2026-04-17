from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure CI/CD Demo"

if __name__ == "__main__":
    app.run()
