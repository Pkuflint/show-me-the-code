#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import re

with open('english.txt', 'r') as f:
    article = f.read()

# 将文本中单词分开
# 这种方法，文章最后一个标点还是会出现空字符串。
word_list = re.split(r'[\,\.\?\;\!\&\s\-\"\"\n\'\(\)]*', article)

print(word_list)
word_dict = {}

for word in word_list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

#print(word_dict)