#! /usr/bin/env python3
# -*- coding:utf-8 -*-

with open('filtered_words.txt', 'r') as f:
    filtered_words = f.read().split('\n')

while True:
    original_words = input('Please input something:')
    has_filtered_word = False
    for word in filtered_words:
        if word in original_words:
            has_filtered_word = True
            break
    if has_filtered_word:
        print('Freedom')
    else:
        print('Human Rights')