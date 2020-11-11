from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

from application.models import Films, Genres

class SameFilmCheck:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        film_list = Films.query.all()
        for film in film_list:
            if field.data == film.title:
                raise ValidationError(self.message)

class FilmForm(FlaskForm):
    film = StringField('Film:',
            validators=[
                DataRequired(),
                    SameFilmCheck(message='That film already exists')
                ]
            )
    length = StringField('Duration: (__hr__mins)')
    #genre = SelectField('Genre',
           # choices=[(genre for genre in genre_list)])
    rating = SelectField('Age Rating',
            choices=[('U','U'),
                    ('PG','PG'),
                    ('12A','12A'),
                    ('12','12'),
                    ('15','15'),
                    ('18','18')
                ]
            )
    submit = SubmitField('Add to database')
