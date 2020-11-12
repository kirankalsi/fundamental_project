from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Films, Genres, FilmGenres
from application.forms import GenreForm, SameGenreCheck, FilmForm, SameFilmCheck

@app.route('/')
def index():
    #genre_list = Genres.query.all()
    #film_list = Films.query.all()
    return render_template('index.html')#, genre_list=genre_list, film_list=film_list)

@app.route('/genre_list')
def genre_list():
    genre_list = Genres.query.all()
    return render_template('genres.html', genre_list=genre_list)

@app.route('/film_list')
def film_list():
    film_list = Films.query.all()
    return render_template('films.html', film_list=film_list)

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
    form.genre.choices = [(genre.id, genre.genre_type) for genre in Genres.query.all()]
    if form.validate_on_submit():
        new_film = Films(title=form.film.data, duration=form.length.data, genre_id=form.genre.data, age_rating=form.ratings.data)
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_film.html', form=form)

@app.route('/update_genre/<int:id>', methods=['GET', 'POST'])
def update_genre(id):
    form = GenreForm()
    genre_to_update = Genres.query.get(id)
    if form.validate_on_submit():
        genre_to_update.genre_type = form.genre.data
        genre_to_update.description = form.description.data
        genre_to_update.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('genre_list'))
    elif request.method == 'GET':
        form.genre.data = genre_to_update.genre_type
        form.description.data = genre_to_update.description
        form.rating.data = genre_to_update.rating
    return render_template('update_genre.html', form=form)

@app.route('/update_film/<int:id>', methods=['GET', 'POST'])
def update_film(id):
    form = FilmForm()
    film_to_update = Films.query.get(id)
    form.genre.choices = [(genre.id, genre.genre_type) for genre in Genres.query.all()]
    if form.validate_on_submit():
        film_to_update.title = form.film.data
        film_to_update.duration = form.length.data
        film_to_update.genre_id = form.genre.data
        film_to_update.age_rating = form.ratings.data
        db.session.commit()
        return redirect(url_for('film_list'))
    elif request.method == 'GET':
        form.film.data = film_to_update.title
        form.length.data = film_to_update.duration
        form.genre.data = film_to_update.genre_id
        form.ratings.data = film_to_update.age_rating
    return render_template('update_film.html', form=form)

@app.route('/delete_genre/<int:id>')
def delete_genre(id):
    genre_to_delete = Genres.query.get(id)
    db.session.delete(genre_to_delete)
    db.session.commit()
    return redirect(url_for('genre_list'))

@app.route('/delete_film/<int:id>')
def delete_film(id):
    film_to_delete = Films.query.get(id)
    db.session.delete(film_to_delete)
    db.session.commit()
    return redirect(url_for('film_list'))
