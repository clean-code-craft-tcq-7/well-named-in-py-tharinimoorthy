# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 06:56:07 2022

@author: TRO1COB
"""
import main

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = main.MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = main.MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(main.MINOR_COLORS) + minor_index + 1

def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)
