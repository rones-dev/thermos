from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")  # dekorator
def index():
    return "yoł yoł działam"


if __name__ == "__main__":
    app.run()
