from flask import Flask

from library.routes import library_bp

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


app.register_blueprint(library_bp)


if __name__ == "__main__":
    app.run(debug=True)
