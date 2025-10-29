from django.test import TestCase

# Create your tests here.

from django.urls import reverse


class ProjectViewTests(TestCase):
	def test_project_view_status_and_content(self):
		"""The /project/ view should return 200 and include 'Group Project' heading."""
		url = reverse('project')
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, 'Group Project')
