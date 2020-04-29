from flask import Flask, render_template

app = Flask(__name__)

# user = "Janusz"
bookmarks = [
    {
        "user": "Zbigniew",
        "url": "https://www.ultradesk.pl",
        "description": "nice IT desk site"
    },
    {
        "user": "Bodzio",
        "url": "mornigstar.pl",
        "description": "star stuff"
    },
    {
        "user": "Helena",
        "url": "https://www.bitbay.net",
        "description": "coins stuff"
    }
]

def get_latest_bookmarks(limit):
    return bookmarks[:limit]

@app.route("/")
@app.route("/index")  # dekorator
def index():
    return render_template("index.html", bookmarks=get_latest_bookmarks(2))     # ile mi sie wyswietli bookmarks


@app.route("/add")
def add():
    return render_template("add.html")


@app.errorhandler(404)
def page_not_founr(e):  # do server not found kasuje
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
