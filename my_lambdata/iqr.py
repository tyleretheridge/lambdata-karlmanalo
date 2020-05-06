# Find the IQR of a set of numbers

import numpy


def iqr(X):
    # Finds midpoint of Q1
    Q1 = numpy.percentile(X, 25, interpolation='midpoint')

    # Finds midpoint of Q3
    Q3 = numpy.percentile(X, 75, interpolation='midpoint')

    # Calculates IQR
    iqr = Q3 - Q1

    return iqr
