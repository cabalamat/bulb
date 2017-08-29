# hypo.py = Hypotheses

from typing import *
from abc import ABC, abstractmethod
from collections import Counter

from butil import *

#---------------------------------------------------------------------

class Hypo(ABC):
    """ a hypothesis """
    
    @abstractmethod
    def call(self, x:str)->str: pass

    @abstractmethod
    def __repr__(self)->str: pass

class NullHypo(Hypo):
    def call(self, x:str)->str: 
        return x
    
    def __repr__(self):
        return "NullHypo()"
    
class AddBefore(Hypo):  
    def __init__(self, prefix):
        self.prefix = prefix
    
    def call(self, x:str)->str: 
        return self.prefix + x
    
    def __repr__(self):
        return form("AddBefore({!r})", self.prefix)  

#---------------------------------------------------------------------

def cost1(y:str, ho:str)->int:
    """ the difference between the actual output from the 
    training set (y) and the output from the hypothesis (ho).
    This is >=0. If y==ho they are the same, otherwise higher score
    mean more difference.
    """
    if y == ho: return 0
    return 100 + charFreqDiff(y, ho) + multiHam(y, ho)

def charFreqDiff(a:str, b:str)->int:
    """ Return the differents in character frequencies between (a)
    and (b).
    For each character, count how many times it appears in (a), how many
    in (b) and add up the differences.
    E.g. charFreqDiff("xxyy","yyxx") => 0
    charFreqDiff("abc","cbdd") => 3 (1 for 'a' plus 2 for 'd')
    """
    ad = dict(Counter(a))
    bd = dict(Counter(b))
    prn("ad={!r} bd={!r}", ad, bd)
    af = sorted(list(ad.items()))
    bf = sorted(list(bd.items()))
    letters = sorted(list(set([c for c, f in af] + [c for c, f in bf])))
    diff = 0
    for letter in letters:
        freqA = ad.get(letter, 0)
        freqB = bd.get(letter, 0)
        diff += abs(freqA - freqB)
    #//for    
    return diff

def multiHam(a:str, b:str)->int:
    if len(a) < len(b):
        a,b = b,a
    if len(b)==0: 
        return len(a)    
    hamVal = min(ham(aSub, b) for aSub in subGroups(a, len(b)))   
    return hamVal + (len(a) - len(b))

def ham(a:str, b:str)->int:
    """ Return the hamming distance between two strings (which must
    be of the same length)
    """
    diffs = 0
    for ca, cb in zip(a,b):
        if ca != cb:
            diffs += 1
    #//for
    return diffs

def subGroups(a:str, size:int)->Iterator[str]:
    for i in range(0, len(a)-size+1):
        yield a[i:i+size]
    #//for    

#---------------------------------------------------------------------

h = NullHypo()

prn("hypo.py h={}", h)
y = h.call("foo")
prn("y={!r}", y)



#end
