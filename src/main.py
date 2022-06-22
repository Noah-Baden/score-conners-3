import argparse
import sys
from os.path import exists

from dcan.Score import do_total_scoring


def main(parents_score_file, age_of_child, sex_of_child, parents_or_teacher):
    results = do_total_scoring(parents_score_file, age_of_child, sex_of_child, parents_or_teacher)
    print(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Score Conners3 exam.')
    parser.add_argument('--input_file_name', type=str, required=True)
    parser.add_argument('--age', type=int, required=True)
    parser.add_argument('--sex', type=str, required=True)
    parser.add_argument('--reporter', type=str, required=True)

    args = parser.parse_args()

    input_file_name = args.input_file_name
    if not exists(input_file_name):
        print(f'File does not exist: {input_file_name}')
        sys.exit(-1)
    sex = args.sex.lower()
    if sex not in ["male", "female"]:
        print("Sex must be 'male' or 'female'")
        sys.exit(-1)
    age = args.age
    if not (8 <= age <= 11):
        print("Age must be between 8 and 11")
        sys.exit(-1)
    reporter = args.reporter
    if reporter not in ["parent", "teacher"]:
        print("Reporter must be 'parent' or 'teacher'")
        sys.exit(-1)

    main(input_file_name, age, sex, reporter)
