# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:29:31 2022

@author: TRO1COB
"""
import main

def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(main.MINOR_COLORS)
    if major_index >= len(main.MAJOR_COLORS):
      raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(main.MINOR_COLORS)
    if minor_index >= len(main.MINOR_COLORS):
      raise Exception('Minor index out of range')
    return main.MAJOR_COLORS[major_index], main.MINOR_COLORS[minor_index]

def test_number_to_pair(pair_number,
                          expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)
  