## A py module for basic stats (because no way in hell am I going to use NumPy
## to just compute averages and standard deviations).
##
## Oh, and a license thingy because otherwise it won't look cool and
## professional.
##
## MIT License
##
## Copyright (c) [2016] [Mehrab Hoque]
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

""" A py module for basic stats.

WARN: This module is not meant to be used in any way besides in the internals of
the spice API source code, but because it is for general statistics, one can
extract this from the API and use it in their own projects.
"""

from __future__ import division
from decimal import Decimal
from collections import Counter
from math import sqrt

def sum(data):
    _data_check(data)
    total = 0
    for elem in data:
        total += Decimal(elem)

    return total

def mean(data):
    _data_check(data)
    return sum(data)/len(data)

def median(data):
    _data_check(data)
    data_len = len(data)
    if data_len % 2 == 0:
        sorted_data = sorted(data)
        return (sorted_data[data_len//2] + sorted_data[data_len//2 - 1])/2
    else:
        return sorted(data)[data_len//2]

def mode(data):
    _data_check(data)
    mode_list = Counter(data)
    return mode_list.most_common(1)[0][0]

def extremes(data):
    _data_check(data)
    return (max(data), min(data))

def p_var(data):
    _data_check(data)
    second_sum = 0
    data_len = len(data)
    mean_val = mean(data)
    for elem in data:
        second_sum += (elem - mean_val) * (elem - mean_val)

    return second_sum/(data_len - 1)

def p_stddev(data):
    _data_check(data)
    return sqrt(p_var(data))

def _data_check(data):
    if len(data) == 0:
        raise ValueError("Data must be non-empty.")
