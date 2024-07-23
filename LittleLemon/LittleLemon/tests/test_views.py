from django.tests import TestCase
from Restaurant import views, models

class MenuViewTest(TestCase):
    def setup(self):
        menu = models.Menu.objects.create(title="MyTitle", price=2.31, inventory=3)
        menu.save()

    def test_getall(self):
        menus = models.Menu.objects.all()
        

