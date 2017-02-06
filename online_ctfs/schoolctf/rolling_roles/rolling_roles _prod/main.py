from hashlib import sha256
from collections import defaultdict

from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify

from users import User, UserManager
import flask.ext.login as flask_login
from flask.ext.login import login_required as authorized

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XXX'

FLAG = 'XXX'
admin = User("administrator", "XXX")
guest = User("guest", "guest")

UM = UserManager()
UM.add_users([admin, guest])

# Mb I should add roles to the User class later
ROLE = {}
ROLE[admin] = "admin"
ROLE[guest] = "guest"
def get_role(user):
    if user in ROLE:
        return ROLE[user]
    else:
        return "user"

# login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return UM.get_by_id(user_id)


@app.route('/')
@authorized
def main_page():
    return render_template('index.html', msg='<h2>Sorry!</h2><p> Our site is under maintenance.</p>')

@app.route('/info')
@authorized
def info_page():
    msg = '''
    <h2>Hello hero!</h2>
    <p>
        There will be some information, according to your status in our team <br>
        <i>Your current status is &lt;%s&gt;</i>
    </p>
    ''' % get_role(flask_login.current_user)
    return render_template('index.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    # POST handler below
    name = request.form['name']
    password = request.form['password']
    if not name or not password:
        return render_template('register.html', msg="Please specify both username and password!")
    user = UM.get_by_name(name)
    if user is not None:
        return render_template('register.html', msg="Sorry, user '%s' already exists!" % name)

    user = User(name, password)
    UM.add_user(user)
    flask_login.login_user(user)
    return redirect(url_for('main_page'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # POST handler below
    name = request.form['name']
    password = request.form['password']
    user = UM.get_by_name(name)
    if user is None:
        return render_template('login.html', msg="No such user!")
    if user.password != sha256(password).hexdigest():
        return render_template('login.html', msg="Wrong password!")

    flask_login.login_user(user)
    next_page = request.args.get('next', '/')
    return redirect(next_page)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    flask_login.logout_user()
    return redirect(url_for('login'))

@app.route('/api/v1/info')
@authorized
def secret():
    msg = {}
    user_role = get_role(flask_login.current_user)
    if user_role == 'admin':
        msg['info'] = FLAG
    elif user_role == 'guest':
        msg['info'] = 'Guests can\'t see team info, sorry!'
    else:
        msg['error'] = 'Unimplemented!'
        if request.args.get('debug', False):
            msg['debug'] = dict(user_roles=["%r" % user for user in ROLE.iterkeys()])
    return jsonify(msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8034, debug=True)
