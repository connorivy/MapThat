from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Document
from .views import *

class DocumentTest(TestCase):
    def create_Document(self, docfile = "filename"):
        return Document.objects.create(docfile = docfile)

    def test_Document_creation(self):
        document = self.create_Document()
        self.assertTrue(isinstance(document, Document))
        self.assertEqual(document.docfile, "filename")

    def test_list_view(self):
        url = reverse("list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_clear_all_view(self):
        url = reverse("clear_all")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_build_kml_view(self):
        url = reverse("build_kml")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)