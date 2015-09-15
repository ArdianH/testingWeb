from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from django.template.loader import render_to_string
from lists.views import home_page


# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)

        expected_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
        #self.assertIn('A new list item', response.content.decode())
        self.assertEqual(response.content.decode(), expected_html)

        ### no testing constant anymore ###
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertIn(b'<title>To-Do lists</title>', response.content)
        #self.assertIn(b'Ardian ', response.content)
        #self.assertTrue(response.content.strip().endswith(b'</html>'))

