from django.tests import TestCase
from Restaurant import models

class MenuTest(TestCase):
    def test_instance(self):
        menu = models.Menu.objects.create(title="MyTitle", price=2.31, inventory=3)
        self.assertEqual(menu, "MyTitle : 2.31")