import unittest

from importlib_metadata import email
from app import db
from app.models import User, Comment

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_Cynthia = User(username = 'Cynthia', password = 'cyn', email = 'oumacynthia817@gmail.com')
        self.new_comment = Comment('absolutely true', pitch_id = 400, user_id = self.user_Cynthia)

    def deleteComment(self):
        Comment.query.delete()
        User.query.delete()

    def test_to_check_variable_instance(self):
        self.assertEqual(self.new_comment.comment, 'Beautiful')
        self.assertEqual(self.new_comment.pitch_id, 400)
        self.assertEqual(self.new_comment.user,self.user_Cynthia)

    def test_to_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
