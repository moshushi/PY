import unittest, os
from mock import patch, Mock

from webparser21 import get_html, BASE_URL, get_html_local
import webparser21


class TestDownl(unittest.TestCase):

    @patch(__name__+".get_html", Mock())
    def test_get_html(self):
        get_html(BASE_URL)
        # Ensure correct url, called once
        get_html.assert_called_once_with\
            ("https://www.weblancer.net/jobs/")


class TestParse(unittest.TestCase):
    def setUp(self):
        self.testdata = webparser21.get_html_local()

    @patch('webparser21.get_html')
#     @patch('get_html')
    def test_get_page_count(self, BASE_URL):
#         get_html.return_value = self.testdata
#         webparser21.get_html.return_value = webparser21.get_html_local()
        webparser21.get_html.return_value = self.testdata
#         get_html.return_value = webparser21.get_html_local()
        self.assertIsInstance(webparser21.get_html_count(BASE_URL), int)
        self.assertIs(webparser21.get_html_count(BASE_URL), 152)

def main():
    unittest.main()
#     get_html_local()

if __name__=='__main__':
    main()
