import flask

app = flask.Flask(__name__)


@app.route('/<word>')
def message(word):
    return word.upper()


if __name__ == '__main__':
    app.run()
