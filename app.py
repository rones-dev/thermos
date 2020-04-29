from flask import Flask, render_template, redirect, url_for, flash
from forms import BookmarkForm
app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xd3g)~5H\xeb\xc1\xe8\xd8\xf8\x05l\xafY\xaf'

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
    return render_template("index.html", bookmarks=get_latest_bookmarks(8))     # ile mi sie wyswietli bookmarks


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookmarkForm()

    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data

        bm = {
            "user": "Agatka",
            "url": url,
            "description": description
        }

        bookmarks.append(bm)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_founr(e):  # do server not found kasuje
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)


# CSRF crros site request for jerry