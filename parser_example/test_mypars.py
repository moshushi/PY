# -*- coding: utf-8 -*-
"""
Unittests for webparser21
"""

import unittest, sys, os, csv
from mock import patch, Mock, mock_open
import webparser21 as wpars

class TestDownl(unittest.TestCase):

    @patch("webparser21.get_html", Mock())
    def test_get_html(self):
        wpars.get_html(wpars.BASE_URL)
        # Ensure correct url, called once
        wpars.get_html.assert_called_once_with\
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
        self.assertIsInstance(wpars.process_page(wpars.BASE_URL), list)

    @patch('webparser21.get_html', Mock())
    def test_parsing_all_page(self):
        wpars.get_html.return_value = self.html_doc
        mock_stdout = Mock()
        sys.stdout = mock_stdout
        data = wpars.parsing_all_page(wpars.BASE_URL)
        self.assertEqual(len(data), 152*20)
        self.assertEqual(data[2], data[22])

    def tearDown(self):
        del self.html_doc
        del self.data_dict


class TestSave(unittest.TestCase):
    def setUp(self):
        self.data_list = [{'title': u'Комплексное продвижение сайта (Игровая тематика: counter strike)',
                           'category': u'Поисковые системы (SEO)',
                           'price': u'',
                           'applications': u'4 заявки'
                           },
                          {'title': u'Реферат по философии на тему "Специфика познания в медицине"',
                           'category': u'Дипломы/Курсовые/Рефераты',
                           'price': u'',
                           'applications': u'исполнитель выбран'
                           },
                          {'title': u'Авторы учебных студенческих работ',
                           'category': u'Дипломы/Курсовые/Рефераты',
                           'price': '$1000',
                           'applications': u'24 заявки'
                           }]

        self.data_dict = {'title': u'Авторы учебных студенческих работ',
                          'category': u'Дипломы/Курсовые/Рефераты',
                          'price': '$1000',
                          'applications': u'24 заявки'
                          }

        self.data_test_list = ["sep=,", 'Проект', 'Категори', 'Цена', 'Заявки',
'Комплексное продвижение сайта (Игровая тематика: counter strike)',
'Поисковые системы (SEO)','','4 заявки',
'Реферат по философии на тему "Специфика познания в медицине"',
'Дипломы/Курсовые/Рефераты','','исполнитель выбран',
'Авторы учебных студенческих работ','Дипломы/Курсовые/Рефераты','$1000',
'24 заявки']

    def test_recode_for_write(self):
        data = wpars.recode_for_write(wpars.NAME_COLUMM)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 4)
        self.assertEqual(data[1], '\xca\xe0\xf2\xe5\xe3\xee\xf0\xe8')

    def test_recode_value_dict(self):
        data = wpars.recode_value_dict(self.data_dict)
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 4)
        self.assertEqual(data['applications'], '24 \xe7\xe0\xff\xe2\xea\xe8')

    def test_save(self):
        with patch('__builtin__.open', mock_open()) as mock_file:
                   wpars.save(self.data_list, wpars.PATH_FILE)
        mock_file.assert_any_call('proje.csv', 'w')
        mock_file.assert_any_call('proje.csv', 'a')


    def test_save_2(self):
        TEST_FILENAME = os.path.join(os.path.dirname(__file__), 'test.csv')
        wpars.save(self.data_list, TEST_FILENAME)
        read_list=[]
        with open(TEST_FILENAME, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                read_list.extend(row)

# reduce both lists to ascii for compare
            list_actual = [x.decode('cp1251') for x in read_list]
            list_example = [x.decode('utf-8') for x in self.data_test_list]

        self.assertSequenceEqual(list_actual, list_example)






def main():
    unittest.main()

if __name__=="__main__":
    main()

