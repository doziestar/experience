from unittest import TestCase
from experience import number_guessing


class GuessGameTest(TestCase):
    def setUp(self):
        pass

    def test_engine(self):
        pass

    def test_local_variable(self):
        self.assertTrue(number_guessing.secret_number, int)
        self.assertIn(number_guessing.secret_number, list(range(20)))
