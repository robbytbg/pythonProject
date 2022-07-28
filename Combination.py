from PSFDD.Triangle import Tri
from PSFDD.Square import square

class comb(Tri,square):
    allsum=square.prod1+Tri.prod2
    print(int(allsum))