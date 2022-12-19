from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        
    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item') # create an item to call id
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'}) # the name is given as if we've just submitted the item form.
        self.assertRedirects(response, '/') # checks if it redirects back home
    
    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}') # perform action by getting it and then applying the change in the link
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id) # item is deleted so no item in db anymore, so length should be 0
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True) # add toggle status
        response = self.client.get(f'/toggle/{item.id}') # provide a toggle change
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
        

