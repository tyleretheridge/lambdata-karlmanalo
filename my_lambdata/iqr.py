# Find the IQR of a set of numbers

import numpy

def iqr(X):
    Q1 = numpy.percentile(X, 25, interpolation='midpoint')
    Q3 = numpy.percentile(X, 75, interpolation='midpoint')

    iqr = Q3 - Q1

    return iqr