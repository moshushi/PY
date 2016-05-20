# -*- coding: utf-8 -*-
"""
Unittests for webparser21
"""

import unittest
from mock import patch, Mock
import webparser21 as wpars

class TestDownl(unittest.TestCase):

    @patch(__name__+".get_html", Mock())
    def _test_get_html(self):
        get_html(BASE_URL)
        # Ensure correct url, called once
        get_html.assert_called_once_with\
            ("https://www.weblancer.net/jobs/")


class TestParse(unittest.TestCase):
    def setUp(self):
        self.html_doc = wpars.get_html_local()
        self.data_dict = {'title': u'Авторы учебных студенческих работ',
                          'category': u'Дипломы/Курсовые/Рефераты',
                          'price': '$1000',
                          'applications': u'24 заявки'
                          }


    def test_get_page_count(self):
        paggination = wpars.get_html_count(self.html_doc)
        self.assertIsInstance(paggination, int)
        self.assertIs(paggination, 152)

    def test_parse(self):
        html = wpars.get_html_local()
        data = wpars.parse(html)
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)
        self.assertEqual(data[2]["price"], '$1000')
        self.assertEqual(data[2]["applications"], u'24 заявки')
        self.assertDictEqual(data[2], self.data_dict)
        self.assertGreater(len(data), 10)

    @patch('webparser21.get_html', Mock())
    def test_process_page(self):
        wpars.get_html.return_value = self.html_doc
        self.assertIsInstance(wpars.process_page(BASE_URL), list)

def main():
    unittest.main()

if __name__=="__main__":
    main()

