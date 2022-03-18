import unittest
import pandas as pd

from dcan.Score import do_total_scoring, get_t_score_from_raw_score


class ScoreTest(unittest.TestCase):
    def test_do_total_scoring(self):
        parents_score_file = "data/sample/inputdata_conners3parent.csv"
        actual_results = do_total_scoring(parents_score_file, 9, "male")
        expected_results = {'LP': (7, 57), 'PR': (0, 44), 'IN': (4, 45), 'AG': (0, 43), 'HY': (1, 40), 'EF': (6, 48)}
        expected_keys = expected_results.keys()
        self.assertEqual(len(expected_keys), len(actual_results.keys()))
        for key in expected_keys:
            self.assertEqual(expected_results[key], actual_results[key])

    def test_do_total_scoring_female_10(self):
        parents_score_file = "data/sample/inputdata_Conners3parent_female10.csv"
        actual_results = do_total_scoring(parents_score_file, 10, "female")
        expected_results = {'LP': (10, 64), 'PR': (10, 90), 'IN': (21, 82), 'AG': (9, 81), 'HY': (12, 67),
                            'EF': (21, 90)}
        # IN (21, 82), HY (12, 67), LP (10, 64), EF (21, 90), AG (9, 81), PR (10, 90)
        expected_keys = expected_results.keys()
        self.assertEqual(len(expected_keys), len(actual_results.keys()))
        for key in expected_keys:
            self.assertEqual(expected_results[key], actual_results[key])

    def test_do_total_scoring_male_10(self):
        parents_score_file = "data/sample/inputdata_Conners3parent_male10.csv"
        actual_results = do_total_scoring(parents_score_file, 10, "male")
        expected_results = {'LP': (12, 69), 'PR': (4, 67), 'IN': (14, 56), 'AG': (6, 67), 'HY': (27, 85),
                            'EF': (11, 57)}
        # SUB-10016-01: IN (14,56), HY (27,85), LP (12,69). EF (11,57). AG (6,67), PR (4,67)
        expected_keys = expected_results.keys()
        self.assertEqual(len(expected_keys), len(actual_results.keys()))
        for key in expected_keys:
            self.assertEqual(expected_results[key], actual_results[key])

    def test_get_t_score_from_raw_score_high(self):
        raw_score = 23
        csv_file = 'data/constant/male_lp.csv'
        df = pd.read_csv(csv_file)
        age = 9
        age_str = str(age)
        column_0_name = 'Unnamed: 0'
        age_column = df[[column_0_name, age_str]]
        scores_df = age_column.rename(columns={"Unnamed: 0": "t-score", age_str: "raw score"})
        t_score = get_t_score_from_raw_score(raw_score, scores_df)
        self.assertEqual(90, t_score)

    def test_get_t_score_from_raw_score_low(self):
        raw_score = 0
        csv_file = 'data/constant/male_lp.csv'
        df = pd.read_csv(csv_file)
        age = 9
        age_str = str(age)
        column_0_name = 'Unnamed: 0'
        age_column = df[[column_0_name, age_str]]
        scores_df = age_column.rename(columns={"Unnamed: 0": "t-score", age_str: "raw score"})
        t_score = get_t_score_from_raw_score(raw_score, scores_df)
        self.assertEqual(40, t_score)


if __name__ == '__main__':
    unittest.main()
