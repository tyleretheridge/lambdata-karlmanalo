# my_lambdata\iqr_oop.py

# IQR function written in terms of OOP

import numpy as np


class IQR():
    def __init__(self):
        self.q1 = np.percentile(self, 25, interpolation='midpoint')
        self.q3 = np.percentile(self, 75, interpolation='midpoint')
    
    def iqr(self):
        print(f'The IQR for this data set is {q3 - q1}')

if __name__ == "__main__":

    data = IQR([1,2,3,4,5])
    print(IQR.iqr)