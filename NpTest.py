import pandas as pd
from pandas.compat import StringIO

temp=u"""TIME             XGSM
2004 006 01 00 01 37 600  1
2004 006 01 00 02 32 800  5
2004 006 01 00 03 28 000  8
2004 006 01 00 04 23 200  11
2004 006 01 00 05 18 400  17"""
#after testing replace StringIO(temp) to filename
df = pd.read_csv(StringIO(temp), 
                 sep="s+", 
                 skiprows=1, 
                 usecols=[0,7], 
                 names=['TIME','XGSM'])

print (df)