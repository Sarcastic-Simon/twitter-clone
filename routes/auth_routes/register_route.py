from flask import request, url_for, render_template, session, flash
from werkzeug.utils import redirect

from services.auth_service import register


def register_route():
    if request.method == 'POST':
        user = register(request.form['username'],
                        request.form['password'])
        if user is not None:
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            flash('Username already taken!', 'errors')
            return redirect(url_for('register'))
    else:
        return render_template('auth/register.html')
