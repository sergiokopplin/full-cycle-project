from dataclasses import is_dataclass
from datetime import datetime
from category.domain.entities import Category
import unittest


class TestCategory(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertEqual(is_dataclass(Category), True)

    def test_constructor_with_optionals(self):
        category = Category('Movie')

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)


    def test_constructor_without_optionals(self):
        created_at = datetime.now()
        category = Category('Movie', 'Some Description', False, created_at)

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some Description')
        self.assertEqual(category.is_active, False)
        self.assertIsInstance(category.created_at, datetime)

    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category('Movie 1')
        category2 = Category('Movie 2')

        self.assertNotEqual(category1.created_at.timestamp(), category2.created_at.timestamp())
