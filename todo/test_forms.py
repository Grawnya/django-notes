from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys()) # to check if name key is in the dictionary of form errors
        self.assertEqual(form.errors['name'][0], 'This field is required.') # To check whether the error message on the name field is "This field is required."

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test todo Item'}) # without done field
        self.assertTrue(form.is_valid())
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm() # empty form
        self.assertEqual(form.Meta().fields, ['name', 'done']) # make sure fields are explicitly defined