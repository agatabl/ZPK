from flask_testing import TestCase
from app.main import db
from manage import app

class BaseTestCase(TestCase):
    """Base Tests"""

    def creapte_app(self):
        app.config.form_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
