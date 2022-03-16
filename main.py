# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dcan.Score import do_scoring, get_t_score


def do_total_scoring():
    parents_score_file = "data/inputdata_conners3parent.csv"
    teacher_score_file = "data/inputdata_conners3parent.csv"
    lookup_table_file = "data/scoringsheet_conners3parent.csv"
    column_name_to_score = do_scoring(parents_score_file, teacher_score_file, lookup_table_file)
    get_t_score(9, 'female', column_name_to_score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    do_total_scoring()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
