import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Genres, Films, FilmGenres
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('DB_URI'),
                SECRET_KEY=getenv('SECRET_KEY'),
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        new_genre = Genres(genre_type='Action', description='A film with a fast-moving plot, usually containing scenes of violence', rating=8)
        new_film = Films(title='Superbad', duration='1hr 59mins', genre_id=3, age_rating='15')
        #db.session.add(new_genre)
        #db.session.add(new_film)
        #db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_genre_list_get(self):
        response = self.client.get(url_for('genre_list'))
        self.assertEqual(response.status_code, 200)

    def test_film_list_get(self):
        response = self.client.get(url_for('film_list'))
        self.assertEqual(response.status_code, 200)

    def test_update_genre_get(self):
        response = self.client.get(url_for('update_genre'))
        self.assertEqual(response.status_code,405)

    def test_update_film_get(self):
        response = self.client.get(url_for('update_film'))
        self.assertEqual(response.status_code,405)

    def test_delete_genre_get(self):
        response = self.client.get(url_for('delete_genre'))
        self.assertEqual(response.status_code,405)

    def test_delete_film_get(self):
        response = self.client.get(url_for('delete_film'))
        self.assertEqual(response.status_code,405)


class TestAdd(TestBase):

    def test_add_genre_post(self):
        response = self.client.post(
            url_for('add_genre'),
            data = dict(
		genre_type='Thriller',
		description='A film that induces strong feelings of excitement, anxiety, tension, suspense, fear, and other similar emotions',
		rating=8)
        )
        self.assertIn(b'Thriller',response.data)

    def test_add_film_post(self):
        response = self.client.post(
            url_for('add_film'),
            data = dict(
		title='Avengers: Endgame',
		duration='3hr 2mins',
		genre_id=8,
		age_rating='12A')
        )
        self.assertIn(b'Avengers: Endgame',response.data)


class TestUpdate_genre(TestBase):

    def test_update_genre_post(self):
        response = self.client.post(
            'update_genre/1',
            data = dict(
		genre_type='International',
		description='Of foreign origin',
		rating=4
		),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)

    def test_update_film_post(self):
        response = self.client.post(
            'update_film/1',
            data = dict(
		title='International',
		duration='Of foreign origin',
		genre_id=5,
		age_rating='15'
		),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)


class TestDelete(TestBase):

    def test_delete_genre_post(self):
        response = self.client.post(
                'delete_genre/<int:id>',
            data = dict(id='1'),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)

    def test_delete_film_post(self):
        response = self.client.post(
            'delete_film/<int:id>',
            data = dict(id='1'),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)
