# bb.py = Black-box functions

#---------------------------------------------------------------------
"""
inputds come in 2 classes:

inputs0 = training set before FP has to guess
inputs1 = training set from 1st guess onwards
"""

class BlackBox:
    
    def getName(self)->str:
        """ return the function's name 
        """
        a = self.__class__.__name__
        return a
    
    def run(self, x:str)->str:
        """ Run the function
        """
        raise NotImplementedError
    
    #===== inputs =====
    
    inputs0 = ['abc', 'aaaaa', '', '1234', 'qwerty']
    inputs1 = ['def', 'VVVV', 'a', 'ww', 'qq', 'rrr', 'stuv']


#---------------------------------------------------------------------

class Doubler(BlackBox): 
    """ duplicate the input """
    def run(self, x):
        return x+x

class Appenda(BlackBox):   
    def run(self, x):
        return x+"a"
    
class Appendz(BlackBox):   
    def run(self, x):
        return x+"z"
    
class RemoveCaps(BlackBox):   
    def run(self, x):
        r = ""
        for ch in x:
            if not ch.isupper():
                r += ch
        return r
    
    inputs = ['abc', 'ABC', 
              'aaaaa', 'VVVVaVaaVaa', '', '1234', 
              'qwerty', 'Qwerty']


#---------------------------------------------------------------------


#end
