from flask import request, url_for, render_template, session, flash
from werkzeug.utils import redirect

from services.user_service import register


def register_route():
    if request.method == 'POST':
        user = register(request.form['username'],
                        request.form['password'])
        if user is not None:
            session['username'] = request.form['username']
            return redirect(url_for('home_page'))
        else:
            flash('Both username and password are required', 'errors')
            return redirect(url_for('register_page'))
    else:
        return render_template('register.html')
