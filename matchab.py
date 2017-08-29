# matchab.py

"""
Abstract superclass for match, plus other classes
"""

from typing import *

#---------------------------------------------------------------------

Example = NamedTuple('Example', [('x', str), ('y', str)])


#---------------------------------------------------------------------

class Match:
    def __init__(self, trainingSet: List[Example]):
        self.trainingSet = trainingSet
    def run(self)->None:
        """ attempt to find a rule that matches all the trainingSet """
     
#---------------------------------------------------------------------


#end