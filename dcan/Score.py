from os.path import exists

import pandas as pd


def do_total_scoring():
    parents_score_file = "data/inputdata_conners3parent.csv"
    # TODO Implement using teacher_score_file
    lookup_table_file = "data/scoringsheet_conners3parent.csv"
    column_name_to_score = do_scoring(parents_score_file, lookup_table_file)
    get_t_score(9, 'female', column_name_to_score)


# TODO Implement for teacher_score_file
def do_scoring(parents_score_file, lookup_table_file):
    parents_scoring_df = pd.read_csv(parents_score_file)
    column_count = parents_scoring_df.size
    column_name_to_score = {}
    lookup_df = pd.read_csv(lookup_table_file)
    lookup_df.fillna('', inplace=True)
    for col in range(5, column_count):
        score = parents_scoring_df.iloc[0][col]
        looked_up_score = lookup_df.iloc[0][score + 1]
        for area_col in range(5, 8):
            column_name = lookup_df.iloc[col - 5][area_col]
            column_name = column_name.strip()
            if column_name:
                if column_name not in column_name_to_score.keys():
                    column_name_to_score[column_name] = looked_up_score
                else:
                    column_name_to_score[column_name] += looked_up_score

    return column_name_to_score


def get_t_score(age, gender, column_name_to_score):
    result = column_name_to_score.copy()
    t_val = -1
    for key in column_name_to_score.keys():
        csv_file = f'data/{gender}_{key.lower()}.csv'
        if not exists(csv_file):
            continue
        df = pd.read_csv(csv_file)
        for row in df[str(age)]:
            row = int(row)
            if row == column_name_to_score[key]:
                t_val = 90 - row
                break
            row += 1
        score = result[key]
        result[key] = (score, t_val)
    return result
