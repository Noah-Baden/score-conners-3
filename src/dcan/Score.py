import math
from os.path import exists

import pandas as pd

QUESTION_OFFSET = 5


def do_total_scoring(parents_score_file):
    # TODO Implement using teacher_score_file
    lookup_table_file = "data/constant/scoringsheet_conners3parent.csv"
    column_name_to_score = do_scoring(parents_score_file, lookup_table_file)
    t_score = get_t_score(9, 'female', column_name_to_score)

    return t_score


# TODO Implement for teacher_score_file
def do_scoring(parents_scores_file, lookup_table_file):
    parents_scores_df = pd.read_csv(parents_scores_file)
    parents_scores_df = parents_scores_df.iloc[:, QUESTION_OFFSET:]
    question_count = parents_scores_df.size
    area_name_to_score = {}
    lookup_df = pd.read_csv(lookup_table_file)
    lookup_df.fillna('', inplace=True)
    for question_number in range(question_count):
        score = parents_scores_df.iloc[0][question_number]
        looked_up_score = lookup_df.iloc[question_number][score + 1]
        for area_col in range(QUESTION_OFFSET, 8):
            area = lookup_df.iloc[question_number][area_col]
            area = area.strip()
            if area:
                if area not in area_name_to_score.keys():
                    area_name_to_score[area] = looked_up_score
                else:
                    area_name_to_score[area] = area_name_to_score[area] + looked_up_score

    return area_name_to_score


def get_t_score(age, gender, column_name_to_score):
    result = {}
    for key in column_name_to_score.keys():
        csv_file = f'data/constant/{gender}_{key.lower()}.csv'
        if not exists(csv_file):
            continue
        df = pd.read_csv(csv_file)
        t_val = 90
        for row in df[str(age)]:
            if math.isnan(row):
                t_val -= 1
                continue
            row = int(row)
            if row <= column_name_to_score[key]:
                break
            t_val -= 1
        score = column_name_to_score[key]
        result[key] = (score, t_val)
    return result
