from django.test import TestCase
from django.urls import reverse
from .models import Details
# Create your tests here.


class HomepageTests(TestCase):
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_contains_correct_html(self):
        self.assertContains(self.response, 'Select a Provider')

    def test_does_not_contain(self):
        self.assertNotContains(self.response, 'I should not be here')


class ViewTests(TestCase):
    def test_view_url_exists_at_desired_location(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

