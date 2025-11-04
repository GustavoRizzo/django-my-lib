from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """Test class to verify the home page is accessible."""
    app_name = 'django_my_lib'

    def test_home_page_status_code(self):
        response = self.client.get(reverse(f"{self.app_name}:home"))
        self.assertEqual(response.status_code, 200)
