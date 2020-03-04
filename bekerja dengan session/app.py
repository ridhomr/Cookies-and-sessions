from flask import Flask, render_template, session, request, redirect, url_for
from models import MPengguna

application = Flask(__name__)
application.config['SECRET_KEY'] = '1234567890'

@application.route('/')
def index():
    if 'username' in session:
            username = session['username']
            return render_template('index.html',
                username=username)
    return redirect(url_for('login'))

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pengguna = MPengguna(username, password)
        if pengguna.authenticate():
            session['username'] = username
            return redirect(url_for('index'))
        msg = 'Username/Password salah'
        return render_template('form.html', msg=msg)
    return render_template('form.html')

@application.route('/logout')
def logout():
    session.pop('username', '')
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)
