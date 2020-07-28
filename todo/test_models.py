from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Default Done Item')
        self.assertFalse(item.done)
