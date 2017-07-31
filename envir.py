# envir.py = environment for FP

from typing import *

from fp import FunPred

""" A LogItem contains (x,y,p) where:
- x: input to BB Function
- y; output from BB function (or None if not available)
- p: prediction by FP of y (or None if not available)
"""
LogItem = Tuple[str, Optional[str], Optional[str]]

""" A Log is a list of Logitems.
These are in chronological order. The last one, which will be
the FP's task, is therefore given by logItem[-1].
"""
Log = List[LogItem]

""" the name of a BB Function is a string """
BBFName = str

#---------------------------------------------------------------------
"""
An environment for a Function predictor
"""


class Environment:
    
    def __init__(self, fp:FunPred):
        self.fp = fp    
        
    def getLog(self)->Log:
        """ The FP asks the environment what its current task is.
        The reply includes information of previous input/output of the
        current BB function.
        """
        
    def getHistory(self)->    
        
        
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
 