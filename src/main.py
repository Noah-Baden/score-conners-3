from dcan.Score import do_total_scoring

if __name__ == '__main__':
    parents_score_file = "data/sample/inputdata_conners3parent.csv"
    t_scores = do_total_scoring(parents_score_file)
    print(t_scores)
