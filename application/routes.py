from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Films, Genres, FilmGenres
from application.forms import FilmForm, SameFilmCheck

@app.route('/')
def index():
    film_list = Films.query.all()
    return render_template('index.html')

@app.route('/add', methods=['GET','POST'])
def add():
    form = FilmForm()
    if form.validate_on_submit():
        new_film = Films(title=form.film.data)
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)
