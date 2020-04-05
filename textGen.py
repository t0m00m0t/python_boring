#! python 3
# textGen.py - テキストファイルを読み込み、特定のキーワードを書き換える

import os,re

keywords = {'ADJECTIVE':'an', 'NOUN':'a', 'ADVERB':'an', 'VERB':'a'}

cwd_dir = os.getcwd()
for filedir in os.listdir(cwd_dir):
    if filedir.endswith('.txt'):
        text_file = open(filedir)
        repl_filename = filedir.split('.')[0] + '_repl.txt'
        repl_file = open(repl_filename, 'w')
        repl_lines = []
        for text_line in text_file.readlines():
            print('Target line ....')
            print(text_line)
            #words = re.split('[.\s]', text_line)
            words = text_line.split()
            for i in range(len(words)):
                print(words[i])
                if words[i][-1] == '.':
                    if words[i][:-1] in keywords.keys():
                        print('Enter {0} {1}:'.format(keywords[words[i][:-1]], words[i][:-1]))
                        words[i] = input()+"."
                elif words[i] in keywords.keys():
                    print('Enter {0} {1}:'.format(keywords[words[i]], words[i]))
                    words[i] = input()
            repl_line = ' '.join(words)
            print('Replaced line ....')
            print(repl_line)
            repl_file.write(repl_line)
        text_file.close()
        repl_file.close()
