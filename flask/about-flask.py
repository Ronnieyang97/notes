import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/user/<name>')
def name(name):
    return '<h1>hello {}<h1>'.format(name)


@app.route('/id/<userid>')
def userid(userid):
    if int(userid) > 100:
        flask.abort(404)
    else:
        return '<h1>hello {}<h1>'.format(userid)


@app.route('/jump')
def jump():
    return flask.redirect('http://127.0.0.1:5000/user/ronnie')


if __name__ == '__main__':
    app.run(debug=True)
