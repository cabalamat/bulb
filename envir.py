# envir.py = environment for FP

from typing import *

from butil import form

import bbfuns
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
class Log:
    def __init__(self, bbName:str, logItems:List[LogItem]):
        self.bbName = bbName
        self.logItems = logItems
        
   def __str__(self):
       s = form("{}\n", self.bbName)
       for x,y,p in self.logItems:
           if p is None:
               strForP = ""
           else:
               strForP = form("({})",ioForPrinting(p)) 
               if y==p:
                   strForP += " -- CORRECT"
           s += form("{}->{} {}\n",
                ioForPrinting(x),   
                ioForPrinting(y), 
                strForP)
       #//for    
       return s



""" the name of a BB Function is a string """
BBFName = str

#---------------------------------------------------------------------
"""
An environment for a Function predictor

instance vars:

currentBbIx = index in bbks of current BB
"""


class Environment:
    
    def __init__(self, fp:FunPred):
        self.fp = fp type: FunPred 
        self.logs = {} # type: Dict[str,Log]
        self.bbks = bbfuns.BB_CLASSES # type: Type[BlackBox]
        self.setBbIx(0)
        
    def setBbIx(ix:int):
        self.currentBbIx = ix # type: int
        currentBbk = self.bbks[self.currentBbIx]
        self.currentBB = currentBkk() # type: BlackBox
        logItems = (
            [(x, self.currentBB.run(x), None) 
             for x in self.currentBB.inputs0]
            + [(x, None, None) 
               for x in self.currentBB.inputs1])
            
            
        currentLog = Log(self.currentBB.getName(), logItems)
        print(
        
        
        
    def getLog(self)->Log:
        """ The FP asks the environment what its current task is.
        The reply includes information of previous input/output of the
        current BB function.
        """
        return self.logs[self.currentBb.getName()]
        
    def getHistory(self)->Dict[str,Log]:
        """ Return all the logs for this environment """
        return self.logs
        
        
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
 