#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    from datetime import datetime

    format_str = '%a %d %b %Y %H:%M:%S %z'

    dt1 = datetime.strptime(t1, format_str)
    dt2 = datetime.strptime(t2, format_str)

    delta = abs(int((dt1 - dt2).total_seconds()))

    return str(delta)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
