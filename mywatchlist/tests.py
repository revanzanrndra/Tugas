from django.test import TestCase, Client
from django.urls import reverse
from .views import *

# Create your tests here.
class MyWatchlistTest(TestCase):
    def test_mywatchlist_url_is_exist(self):
        response = Client().get(reverse('mywatchlist:show_watchlist'))
        self.assertEqual(response.status_code, 200)

    def test_mywatchlist_uses_watchlist_html(self):
        response = Client().get(reverse('mywatchlist:show_watchlist'))
        self.assertTemplateUsed(response, 'watchlist.html')

class DataDeliveryTest(TestCase):
    def test_html_url_is_exist(self):
        response = Client().get(reverse('mywatchlist:show_html'))
        self.assertEqual(response.status_code, 200)
    
    def test_xml_url_is_exist(self):
        response = Client().get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code, 200)
    
    def test_json_url_is_exist(self):
        response = Client().get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code, 200)