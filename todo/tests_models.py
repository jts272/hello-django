from django.test import TestCase
from .models import Item

# Create your tests here.

# We don't need to test internal Django code - the devs already have
# We can test that our items will default to is_done=False


class TestModels(TestCase):
    def test_is_done_defaults_to_false(self):
        # Simply instantiate the item
        item = Item.objects.create(name='Test todo item')
        # Assert that the is_done status is false
        self.assertFalse(item.is_done)

    def test_item_string_method_returns_name(self):
        # Instantiate the item
        item = Item.objects.create(name='Test todo item')
        # Confirm this name is returned when we render item as a string
        # Uses type coercion
        self.assertEqual(str(item), 'Test todo item')
