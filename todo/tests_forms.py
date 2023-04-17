from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        # Instantiate the form
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        # Invalid forms should return dict of error messages
        # Create specific assert for if the key is in the dict
        self.assertIn('name', form.errors.keys())
        # Check specific content of error message
        # Zero index required as form returns list of errors
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_is_done_field_is_not_required(self):
        # Provide only a name and not a required status on is_done
        form = ItemForm({'name': 'Test todo status'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # Protect against future changes to the model by checking we
        # only display the fields we want to, explicitly and in order
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'is_done'])
