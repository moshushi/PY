import unittest
from mock import patch

from webparser21 import get_html, BASE_URL


class TestDownl(unittest.TestCase):

    def test_get_html(self):
        with patch(__name__+".get_html") as patched_get_html:
            get_html(BASE_URL)
            # Ensure correct url, called once
            patched_get_html.assert_called_once_with\
                ("https://www.weblancer.net/projects/")

def main():
    unittest.main()

if __name__=='__main__':
    main()

