# my_lambdata\my_script.py

import pandas

#from my_mod import enlarge
from my_lambdata.my_mod import enlarge

print("HELLO WORLD")

print(2+2)

df = pandas.DataFrame({"a":[1,2,3],"b":[4,5,6]})
print(df.head())

y = 9
print(enlarge(y))