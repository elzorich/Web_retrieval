"""
Authors:
Alena Zorich (elzorich@uni-koblenz.de)
Igor Maksimovich Fedotov (ifedotov@uni-koblenz.de)
Mariya Chkalova (mchkalova@uni-koblenz.de)
Arsenii Smyrnov (smyrnov@uni-koblenz.de)
"""

#!/usr/bin/env python3

import unittest
from naive_search import *


class TestNaiveSearch(unittest.TestCase):
    DEVEL_CORPUS = 'simplewiki-20160501-extracted-devel.xml'

    def test_search_test(self):
        expected_matches = {'Wikipedia:Basic English alphabetical wordlist',
                            'Biology', 'Computer science', 'Creator'}
        actual_matches = naive_search(self.DEVEL_CORPUS, 'test')
        print(expected_matches)
        print(actual_matches)
        self.assertEqual(expected_matches, actual_matches)

    def test_search_simple(self):
        expected_matches = {'A', 'Wikipedia:Administrators', 'Australia',
                            'Apple', 'Algebra', 'Astronomy',
                            'Wikipedia:Basic English alphabetical wordlist',
                            'Boot device', 'Berry', 'Chemistry',
                            'Computer science', 'Wikipedia:Wikipedia down',
                            'Computer', 'Cartography', 'Creativity',
                            'Calculus'}
        actual_matches = naive_search(self.DEVEL_CORPUS, 'simple')
        self.assertEqual(expected_matches, actual_matches)

    def test_search_case_insensitive(self):
        matches1 = naive_search(self.DEVEL_CORPUS, 'simple')
        matches2 = naive_search(self.DEVEL_CORPUS, 'Simple')
        matches3 = naive_search(self.DEVEL_CORPUS, 'SIMPLE')
        matches4 = naive_search(self.DEVEL_CORPUS, 'sImPlE')
        self.assertEqual(matches1, matches2)
        self.assertEqual(matches1, matches3)
        self.assertEqual(matches1, matches4)

    def test_empty_keyword(self):
        self.assertEqual(set(), naive_search(self.DEVEL_CORPUS, ''))

    def test_search_without_results(self):
        self.assertEqual(set(), naive_search(self.DEVEL_CORPUS, 'adiufdsafan'))


if __name__ == '__main__':
    unittest.main()
