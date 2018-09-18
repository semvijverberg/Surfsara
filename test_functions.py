#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:44:52 2018

@author: semvijverberg
"""
import functions
from mock import patch, Mock


#def test_awesome_function():
#    expected_value = 42
#    actual_value = func.awesome_function()
#    assert expected_value == actual_value, "value does not match"
#
#
#def test_something_else():
#    assert 1 == 2, "Failing test"
#
#def test_something():
#    assert 2 == 2, "Succeding test"   
    

# =============================================================================
# Avoid some heavy duty computation within your tests with MOCK
# =============================================================================

# could be that we don't want to actually download the text from web. To ensure 
# this, we mock the function. (circumvent that it downloads). 
# mock is a python module "conda install -c conda-forge mock"

@patch("requests.get")
def test_do_text_analysis(mock_call):
    mock_call.return_value = Mock()
    mock_call.return_value.text  = 'Some mock text'
    
    wc = functions.do_text_analysis()
    assert wc > 0, 'Text should have more then 0 words'




# import text from web
#import requests
#requests.get('https://python-mock-tutorial.readthedocs.io/en/latest/mock.html')
#r = requests.get('https://python-mock-tutorial.readthedocs.io/en/latest/mock.html')
#r.text


