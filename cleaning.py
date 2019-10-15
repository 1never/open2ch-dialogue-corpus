# -*- coding: utf-8 -*-
import argparse


def include_ng(line, ng_words):
    line = line.lower()
    for w in ng_words:
        if w in line:
            return True
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default=None, type=str, required=True,
                        help="The input tsv file.")
    parser.add_argument("--output_file", default=None, type=str, required=True,
                        help="The output tsv file.")
    args = parser.parse_args()

    ng_words = []
    with open("data/ng_words.txt") as f:
        for line in f:
            ng_words.append(line.strip())


    cleaned_lines = []
    with open(args.input_file) as f:
        for l in f:
            l = l.strip()
            while include_ng(l, ng_words):
                l = l.rsplit("\t", 1)[0]
                if "\t" not in l:
                    break
            if "\t" in l:
                cleaned_lines.append(l + "\n")
    w = open(args.output_file, "w")
    w.writelines(cleaned_lines)
    w.close()
