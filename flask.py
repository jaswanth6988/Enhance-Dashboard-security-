from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure Dashboard Access!"

if __name__ == "__main__":
    # Run with SSL/TLS
    app.run(ssl_context=("cert.pem", "key.pem"), debug=True)
