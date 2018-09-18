#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:44:42 2018

@author: semvijverberg
"""

import requests

def awesome_function():
    print('Do some heavy calculation!')
    return 40 + 1

def download_text_from_web():
    print("pretend we download something")
    return 'Text we got form the web'

def countWords(text):
    return len(text)


def do_text_analysis():
    r = requests.get('https://python-mock-tutorial.readthedocs.io/en/latest/mock.html')
    print(r.text)
    word_count = countWords(r.text)
    return word_count

do_text_analysis()
