from flask import request, session, url_for, render_template, flash
from werkzeug.utils import redirect

from services.user_service import login


def login_route():
    if request.method == 'POST':
        user = login(request.form['username'],
                     request.form['password'])
        if user is not None:
            session['username'] = request.form['username']
            return redirect(url_for('home_page'))
        else:
            flash('Incorrect credentials', 'errors')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')
