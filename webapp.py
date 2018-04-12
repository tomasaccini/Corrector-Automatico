import flask
import os

app = flask.Flask(__name__)
app.secret_key = os.urandom(12)

webapp_password = os.environ['WEBAPP_PASSWORD']
webapp_user = os.environ['WEBAPP_USER']


@app.route('/')
def index():
    if not flask.session.get('logged_in'):
        return flask.render_template('login.html')
    else:
        return flask.render_template("index.html")


@app.route('/login', methods=('GET', 'POST'))
def login():
    if flask.request.form['password'] == webapp_password and flask.request.form['username'] == webapp_user:
        flask.session['logged_in'] = True
    return index()