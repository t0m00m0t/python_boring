#! Python 3
# regexSearch.py - フォルダの中のすべての.txtファイルを開いて、ユーザーが指定した正規表現に合致する行を検索し、結果を画面に表示する

import re, os

print('Input regex :')
input_regex = input()

print('Input replaced word :')
repl_word = input()

# 正規表現
regex = re.compile(repl(input_regex))

# フォルダの中のtxt探索
for filedir in os.listdir(os.getcwd()):
    if filedir.endswith('.txt'):
        text_file = open(filedir)
        for line in text_file.readlines():
            mo = regex.search(line)
            if mo != none:
                print('Found regex maching !!!')
                print(line)
        text_file.close()
