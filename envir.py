# envir.py = environment for FP

from fp import FunPred


#---------------------------------------------------------------------
"""
An environment for a Function predictor
"""


class Environment:
    
    def __init__(self, fp:FunPred):
        self.fp = fp
        
    def getTask(self):
        """ The FP asks the environment what its current task is.
        The reply includes information of previous input/output of BB 
        functions.
        """
        
    def makePrediction(self, bbfn:str, x:str, p:str)->str:
        """ The FP informs the environment of its prediction of
        the current task.
        bbfn = name of BB function
        x = input to function
        p = FP's predicted output from function
        return = actual output from function
        """
    
    
    

#---------------------------------------------------------------------

def registerFP(fp:FunPred)->Environment:
    """ register a function predictor """
    env = Environment(fp)
    return env
    


#---------------------------------------------------------------------


#end
 