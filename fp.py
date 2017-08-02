# fp.py = function predictor abstract class

class FunPred(metaclass=ABCMeta):
    
    @abstractmethod
    def getName(self)->str: pass
        

#end
