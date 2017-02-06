from flask import flash, redirect, render_template, url_for
from sqlalchemy import exc
import datetime

from . import home
from .forms import VisitForm
from .. import db
from ..models import Visit

@home.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage on the / route
    """
    form = VisitForm()

    if form.validate_on_submit():
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        visit = Visit(name=form.name.data, sid=form.sid.data, visitdate=time)

        # add visit to database
        db.session.add(visit)
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            flash("Hmmm... Something's not quite right")
        #flash('Welcome to Office Hours!')

        return redirect(url_for('home.welcome'))

    return render_template('home/index.html', form=form, title="Sign In")

@home.route('/welcome', methods=['GET', 'POST'])
def welcome():
    """
    Render the homepage on the /welcome route
    """
    return render_template('home/welcome.html', title="Welcome")
