# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:46:33 2022

@author: TRO1COB
""" 
class Printing:

    def color_pair_to_string(major_color,minor_color):
        c=0;
        for i in (major_color):
            for j in (minor_color):
                c+=1
                print (f'{c} {i} {j}')
