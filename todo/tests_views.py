from django.test import TestCase
# Perform CRUD operations in Django tests by importing models
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    def test_get_todo_list(self):
        # Use Django HTTP client from testing framework to instantiate
        response = self.client.get('/')
        # Check against successful HTTP response code
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # Edit page requires an id in the url after '/edit/'
        # If we supply a static number, the test will pass only if the
        # number happens to be in the database
        #
        # Instantiate a db entry
        item = Item.objects.create(name='Test todo item')
        # Use f string to check for the id of this newly created item in
        # the url
        response = self.client.get(f'/edit/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add/', {'name': 'Test added item'})
        # View should redirect home when successful
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # Create item first, using same syntax as the edit test
        item = Item.objects.create(name='Test todo item')
        response = self.client.get(f'/delete/{item.id}/')
        self.assertRedirects(response, '/')
        # Try to get the item id we just created from the db
        # id comes from Django automatically
        existing_items = Item.objects.filter(id=item.id)
        # Then check that the iterable returned is empty
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # Instantiate an item with the is_done status checked
        item = Item.objects.create(name='Test todo item', is_done=True)
        response = self.client.get(f'/toggle/{item.id}/')
        self.assertRedirects(response, '/')
        # After the redirect, get the item we instantiated by id
        updated_item = Item.objects.get(id=item.id)
        # Then check its initial is_done status of True is now False
        self.assertFalse(updated_item.is_done)
