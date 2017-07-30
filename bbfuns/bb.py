# bb.py = Black-box functions

#---------------------------------------------------------------------

class BlackBox:
    
    def getName(self):
        """ return the function's name 
        """
        a = self.__class__
        b = a.__name__
        print "a=%r b=%r" % (a,b)
        return b
    
    def run(self, x):
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
