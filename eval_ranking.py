# -*- coding: utf-8 -*-
import numpy as np
import argparse

def recall_at_k(y_true, y_pred, k):
    correct = 0
    total = 0
    for yt, yp in zip(y_true, y_pred):
        total += 1
        for i in yp.argsort()[::-1][0:k]:
            if yt[i] == 1:
                correct += 1
    return correct / total

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default=None, type=str, required=True,
                        help="The input dev or test tsv file.")
    parser.add_argument("--score_file", default=None, type=str, required=True,
                        help="The estimated score file.")
    args = parser.parse_args()

    y_input = []
    with open(args.input_file) as f:
        for l in f:
            if "\t" in l:
                y_input.append(int(l.split("\t")[0]))


    y_score = []
    with open(args.score_file) as f:
        for l in f:
            l = l.strip()
            if len(l) > 0:
                y_score.append(float(l))
    assert len(y_input) == len(y_score), "行数が一致しません． input: {0}, score: {1}".format(len(y_input), len(y_score))
    y_input = np.array(y_input).reshape(-1, 10)
    y_score = np.array(y_score).reshape(-1, 10)
    for k in range(1, 11):
        print("1 in 10 Recall@" + str(k) + ": " + str(recall_at_k(y_input, y_score, k)))
