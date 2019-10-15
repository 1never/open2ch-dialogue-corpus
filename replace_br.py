# coding: UTF-8
import MeCab
import re
import argparse

mecab = MeCab.Tagger()
mecab.parse('')

symbols = ["w", "ｗ", "。", "、", "，", "．", ",", ".", ")", "）", "？", "！", "?", "!", "…", "」"]

def last_word_pos(text):
    node = mecab.parseToNode(text)
    pos = None
    while node:
        if "BOS" not in node.feature:
            pos = node.feature
        node = node.next
    return pos

def replace_br(line):
    # 各文の先頭の改行記号は削除
    tmp = ""
    for l in line.split("\t"):
        tmp += re.sub(r'^( )+(__BR__ )+', '', l) + "\t"
    line = re.sub(r'\t$', "", tmp)

    if "__BR__" not in line:
        return line
    else:
        # 改行記号が3つ連続の場合は2個に置換
        line = line.replace(" __BR__ __BR__ __BR__ ", " __BR__ __BR__ ")
        # 改行記号が2つ連続の場合は，直前にsymbolsの記号があれば改行記号を削除．なければ句点に置換．
        if " __BR__ __BR__ " in line:
            tmp_line = ""
            ls = line.split(" __BR__ __BR__ ")
            for i in range(len(ls)-1):
                l = ls[i]
                contains_symbol = False
                for s in symbols:
                    if l.endswith(s):
                        contains_symbol = True
                if contains_symbol:
                    tmp_line += l
                else:
                    tmp_line += l + "。"
            tmp_line += ls[-1]
            line = tmp_line

        # 改行記号が存在する場合は，直前にsymbolsの記号があれば削除．
        # 改行記号の直前の語が係助詞，格助詞，接続助詞の場合は読点，それ以外は句点に置換，
        if " __BR__ " in line:
            tmp_line = ""
            ls = line.split(" __BR__ ")
            for i in range(len(ls)-1):
                l = ls[i]
                contains_symbol = False
                for s in symbols:
                    if l.endswith(s):
                        contains_symbol = True
                if contains_symbol:
                    tmp_line += l
                else:
                    lwpos = last_word_pos(l)
                    if "係助詞"in lwpos or "格助詞" in lwpos or "接続助詞" in lwpos:
                        tmp_line += l + "、"
                    else:
                        tmp_line += l + "。"
            tmp_line += ls[-1]
            line = tmp_line
    return line


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default=None, type=str, required=True,
                        help="The input tsv file.")
    parser.add_argument("--output_file", default=None, type=str, required=True,
                        help="The output tsv file.")
    args = parser.parse_args()

    nobr_lines = []
    with open(args.input_file) as f:
        for l in f:
            l = l.strip()
            nobr_lines.append(replace_br(l) + "\n")

    w = open(args.output_file, "w")
    w.writelines(nobr_lines)
    w.close()


if __name__ == '__main__':
    main()

