from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Films, Genres, FilmGenres
from application.forms import GenreForm, SameGenreCheck, FilmForm, SameFilmCheck

@app.route('/')
def index():
    genre_list = Genres.query.all()
    film_list = Films.query.all()
    return render_template('index.html', genre_list=genre_list, film_list=film_list)

@app.route('/add_genre', methods=['GET','POST'])
def add_genre():
    form = GenreForm()
    if form.validate_on_submit():
        new_genre = Genres(genre_type=form.genre.data, description=form.description.data, rating=form.rating.data)
        db.session.add(new_genre)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_genre.html', form=form)

@app.route('/add_film', methods=['GET','POST'])
def add_film():
    form = FilmForm()
    if form.validate_on_submit():
        new_film = Films(title=form.film.data)
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_film.html', form=form)
