import unittest

from dcan.Score import do_total_scoring


class ScoreTest(unittest.TestCase):
    def test_do_total_scoring(self):
        parents_score_file = "data/sample/inputdata_conners3parent.csv"
        actual_results = do_total_scoring(parents_score_file)
        expected_results = {'LP': (7, 56), 'PR': (5, 66), 'IN': (10, 59), 'AG': (14, 90), 'HY': (14, 64), 'EF': (7, 53)}
        expected_keys = expected_results.keys()
        self.assertEqual(len(expected_keys), len(actual_results.keys()))
        for key in expected_keys:
            self.assertEqual(expected_results[key], actual_results[key])

if __name__ == '__main__':
    unittest.main()
