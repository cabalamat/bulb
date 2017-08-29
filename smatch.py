# smatch.py = a simple match

from typing import *

import matchab
from matchab import Match, Example


#---------------------------------------------------------------------

class SimpleMatch(Match):

    def __init__(self, trainingSet: List[Example]):
        super().__init__()
        
        #...initialisation for SimpleMatch...

    def run(self)->None:
        print "finished"

#---------------------------------------------------------------------

#end
