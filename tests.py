import time
import unittest

from string_finder import Finder


class TestStringFinder(unittest.TestCase):

    def test_valid_str(self):
        finder = Finder(['python', 'django', 'flask', 'unit', 'test'])
        response = finder.find('thonpy')
        self.assertEqual(['python'], response)

    def test_invalid_str(self):
        finder = Finder(['python', 'django', 'flask', 'unit', 'test'])
        response = finder.find('java')
        self.assertEqual([], response)

    def test_empty_str(self):
        finder = Finder(['python', 'django', 'flask', 'unit', 'test'])
        response = finder.find('')
        self.assertEqual([], response)

    def test_with_none(self):
        finder = Finder(['python', 'django', 'flask', 'unit', 'test'])
        response = finder.find(None)
        self.assertEqual([], response)

    def test_with_empty_data(self):
        finder = Finder([])
        response = finder.find('python')
        self.assertEqual([], response)

    def test_with_duplicate_data_entries(self):
        finder = Finder(['python', 'django', 'flask', 'unit', 'test', 'thonpy'])
        response = finder.find('thynop')
        self.assertEqual(['python', 'thonpy'], response)

    def test_with_uppercase_str(self):
        finder = Finder(['python', 'django', 'flask', 'unit', 'test', 'thonpy'])
        response = finder.find('PYTHON')
        self.assertEqual([], response)

    def test_with_duplicating_characters(self):
        finder = Finder(['python', 'django', 'flask', 'unit', 'test', 'thonpy'])
        response = finder.find('pythoooon')
        self.assertEqual([], response)


class TestPerformanceStringFinder(unittest.TestCase):
    """
    Tests to determine the performance of the Finder. setUp & tearDown methods are here
    used to see for the time our solution is taking with different use cases and sizes
    of the data.
    """

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

    def test_with_huge_list(self):
        finder = Finder(['python', 'django', 'flask', 'unit', 'test']*100000)
        response = finder.find('thonpy')
        self.assertEqual(['python']*100000, response)
