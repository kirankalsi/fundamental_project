from application import db

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float), nullable=False)
    film-genres = db.relationship('FilmGenres', backref='genre')

class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.String(20), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    age_rating = db.Column(db.String(5), nullable=False)
    film-genres = db.relationship('FilmGenres', backref='film')

class FilmGenres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'), nullable=False)
