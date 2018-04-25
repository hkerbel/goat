from django.test import TestCase

from lists.forms import EMPTY_ITEM_ERROR, ItemForm
from lists.models import List, Item


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        #####self.fail(form.as_p()) [hjk: I *think* this was removed for TDD Goat's code since his tests
        # all pass. Anyway, commedt out for now. Currently on chapter 14.2 - Using the form in our views.
        # Apr 24, 2018]

    def test_form_item_imput_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'], [EMPTY_ITEM_ERROR]
        )

    def test_home_page_uses_item_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], ItemForm)


    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()        
        form = ItemForm(data={'text': 'do me'})        
        new_item = form.save(for_list=list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list, list_)

