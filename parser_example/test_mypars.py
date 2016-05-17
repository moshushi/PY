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
        self.soup = webparser21.BeautifulSoup(self.testdata, 'html.parser')

    @patch('webparser21.get_html')
    def test_get_page_count(self, BASE_URL):
        webparser21.get_html.return_value = self.testdata
        self.assertIsInstance(webparser21.get_html_count(BASE_URL), int)
        self.assertIs(webparser21.get_html_count(BASE_URL), 152)


    def test_parse_table_have_tag(self):
        soup = self.soup
        check_tag = len(soup.find('div', class_="container-fluid \
                                  cols_table show_visited"))
        # Ensure soup have tag table
#         self.assertIsInstance(check_tag, <class "bs4.element.Tag"))
        self.assertIsInstance(check_tag, int)


#     @patch(__name__+"parse", Mock())
    def test_parse_table_correct_call(self):
        # how we can check correct tag in soup.find for table?
        pass




def main():
    unittest.main()
#     get_html_local()

if __name__=='__main__':
    main()
