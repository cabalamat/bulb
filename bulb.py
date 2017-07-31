# bulb.py = FP implementation

import bbfuns


#---------------------------------------------------------------------

def ioForPrinting(s:str)->str:
    """ format an input or output string for printing """
    specialChars = "->\"'\\,;\n" 
    if s:
        containsSpecial = any(ch in specialChars for ch in s)
    else:    
        containsSpecial = True
    if containsSpecial:
        s = repr(s)
    return s    

#---------------------------------------------------------------------

def main():
    for bbk in bbfuns.BB_CLASSES:
        bbf = bbk()
        print("===== {} =====".format(bbf.getName()))
        inputs = bbf.inputs
        #print("Inputs are: {}".format(inputs))
        for x in inputs:
            y = bbf.run(x)
            print("{} -> {}".format(
                ioForPrinting(x), ioForPrinting(y)))
        #//for x    
    #//for    

#---------------------------------------------------------------------

if __name__=='__main__':
    main()

#end
