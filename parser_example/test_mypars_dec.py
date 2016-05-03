import unittest
from mock import patch, Mock

from webparser21 import get_html, BASE_URL


class TestDownl(unittest.TestCase):

    @patch(__name__+".get_html", Mock())
    def test_get_html(self):
        get_html(BASE_URL)
        # Ensure correct url, called once
        get_html.assert_called_once_with\
            ("https://www.weblancer.net/projects/")

def main():
    unittest.main()

if __name__=='__main__':
    main()
