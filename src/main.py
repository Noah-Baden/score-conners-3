import argparse
import sys
from os.path import exists

from dcan.Score import do_total_scoring


def main(parents_score_file, age, sex):
    results = do_total_scoring(parents_score_file, age, sex)
    print(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Score Conners3 exam.')
    parser.add_argument('--parents_file_name', type=str, required=True)
    parser.add_argument('--sex', type=str, required=True)
    parser.add_argument('--age', type=int, required=True)

    args = parser.parse_args()

    parents_file_name = args.parents_file_name
    if not exists(parents_file_name):
        print(f'File does not exist: {parents_file_name}')
        sys.exit(-1)
    sex = args.sex.lower()
    if not sex in ["male", "female"]:
        print("Sex must be 'male' or 'female'")
        sys.exit(-1)
    age = args.age
    if not (8 <= age <= 11):
        print("Age must be between 8 and 11")
        sys.exit(-1)

    main(parents_file_name, age, sex)
