import unittest

from dcan.Score import do_total_scoring


class ScoreTest(unittest.TestCase):
    def test_do_total_scoring(self):
        parents_score_file = "data/sample/inputdata_conners3parent.csv"
        actual_results = do_total_scoring(parents_score_file)
        expected_results = {'LP': (7, 57), 'PR': (0, 44), 'IN': (4, 45), 'AG': (0, 43), 'HY': (1, 40), 'EF': (6, 48)}
        expected_keys = expected_results.keys()
        self.assertEqual(len(expected_keys), len(actual_results.keys()))
        for key in expected_keys:
            self.assertEqual(expected_results[key], actual_results[key])

if __name__ == '__main__':
    unittest.main()
