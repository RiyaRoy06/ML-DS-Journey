# Goal: Group list of dicts by "category".

from itertools import groupby
d=sorted('aeffdaabbc')
for i,j in groupby(d):
   print(i,list(j))
