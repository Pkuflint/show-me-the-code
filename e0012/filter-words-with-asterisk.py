#! /usr/bin/env python3
# -*- coding:utf-8 -*-

with open('filtered_words.txt', 'r') as f:
    filtered_words = f.read().split('\n')

while True:
    original = input('Please input something: ')

    for word in filtered_words:
        if word in original:
            original = original.replace(word, '*' * len(word))
    print(original)
