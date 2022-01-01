
from flask import request
def reserch4letters(py_vowels,py_word):
    py_vowels = request.form['vowels']
    py_word = request.form['word']
    py_found = {}
    for i in py_word:
        if i in py_vowels:
            # 初始化 setdefault
            py_found.setdefault(i, 0)
            py_found[i] += 1
    return py_found