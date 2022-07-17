from datetime import datetime
from category.domain.entities import Category
import unittest


class TestCategory(unittest.TestCase):

    def test_constructor(self):
        category = Category('Movie', 'Some Description', True, datetime.now())

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some Description')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)
