from unicodedata import category
import unittest

from importlib_metadata import email
from app import db
from app.models import User, Pitch

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.user_Cynthia = User(username = 'Cynthia', password = 'cyn', email = 'oumacynthia817@gmail.com')
        self.new_pitch = Pitch(title = 'Love', post = 'Love is a beautiful thing', category = 'events', user= self.user_Cynthia)

    def deleteComment(self):
        Pitch.query.delete()
        User.query.delete()

    def test_to_check_variable_instance(self):
        self.assertEqual(self.new_pitch.title, 'Love')
        self.assertEqual(self.new_pitch.post, 'Love is a beautiful thing')
        self.assertEqual(self.new_pitch.category,'event')
        self.assertEquals(self.new_pitch.user,self.user_Cynthia)

    def test_to_save_pitch(self):
        self.new_pitch.save_review()
        self.assertTrue(len(Pitch.query.all())>0)
