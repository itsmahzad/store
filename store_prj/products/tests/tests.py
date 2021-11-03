from django.test import TestCase
from products.models import Clothing
from django.utils import timezone
from django.urls import reverse

class ClothingModelTest(TestCase):

    def create_clothing(self, title="only a test", body="yes, this is only a test"):
        return Clothing.objects.create(title=title, body=body, created_at=timezone.now())

    def test_clothing_creation(self):
        w = self.create_clothing()
        self.assertTrue(isinstance(w, Clothing))
        self.assertEqual(w.__unicode__(), w.title)