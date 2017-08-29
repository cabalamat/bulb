# test_hypo.py = test <hypo.py>


import lintest

import hypo
from hypo import *

#---------------------------------------------------------------------

class T_functions(lintest.TestCase):
    
    def test_charFreqDiff(self):
        r = charFreqDiff("abc", "abc")
        self.assertSame(r, 0)
        
        r = charFreqDiff("", "")
        self.assertSame(r, 0)
        
        r = charFreqDiff("aaabbc", "bbbxxxz")
        self.assertSame(r, 9)
        
        r = charFreqDiff("1.3.4.4", "...4431")
        self.assertSame(r, 0)
        
    def test_cost1(self):
        r = cost1("abc", "abc")
        self.assertSame(r, 0)
        
        r = cost1("abc", "xabc")
        self.assertSame(r, 101)
        
        r = cost1("abc", "cba")
        self.assertSame(r, 100)
        
    def test_subGroups(self):
        r = list(subGroups("abcde", 3))
        sb = ["abc", "bcd", "cde"]
        self.assertSame(r, sb)



#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_functions)

if __name__=='__main__': group.run()





#end
