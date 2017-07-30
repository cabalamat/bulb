# bb.py = Black-box functions

#---------------------------------------------------------------------

class BlackBox:
    
    def getName(self)->str:
        """ return the function's name 
        """
        a = self.__class__.__name__
        return a
    
    def run(self, x:str)->str:
        """ Run the function
        """
        raise ImplementedBySubclass


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


#---------------------------------------------------------------------


#end
