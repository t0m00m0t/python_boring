#! python 3
# mcb.pyw
# Usage
# mcb.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
# mcb.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# mcb.pyw list - 全キーワードをクリップボードにコピー
# mcb.pyw delete <keyword> - キーワードに紐づけられたテキストを削除する
# mcb.pyw delete - 全キーワードを削除する

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3:
    if sys.argv[1].lower == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower == 'delete':
        del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # キーワード一覧と内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif sys.argv[1] == 'delete':
        mcb_shelf.clear()
mcb_shelf.close()
