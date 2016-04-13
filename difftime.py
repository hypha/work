#!/usr/bin/env python
__author__ = 'raquel'

import datetime

def diff_time():
    start = raw_input("start time: ")
    end = raw_input("end time: ")
    FMT = '%H:%M'
    start_time = datetime.datetime.strptime(start, FMT)
    end_time = datetime.datetime.strptime(end, FMT)
    diff_time = end_time - start_time
    return diff_time

print "Time difference is %s" % diff_time()