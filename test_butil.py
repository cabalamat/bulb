# test_butil.py = test butil.py

import lintest

import butil
from butil import *

#---------------------------------------------------------------------


class T_strFunctions(lintest.TestCase):
    
    def test_form(self):
        prn("^^^ test_form ^^^")
        r = butil.form("abcde")
        self.assertSame(r, "abcde")
        
        r = butil.form("abcde {} {}", "www", 234)
        self.assertSame(r, "abcde www 234")
        
        r = butil.form("abcde {x} {y}", x="www", y=234)
        self.assertSame(r, "abcde www 234")
        
        r = butil.form(":{} {x} {y}", "qwert", x="www", y=234)
        self.assertSame(r, ":qwert www 234")


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_strFunctions)

if __name__=='__main__': group.run()



#end