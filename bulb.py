# bulb.py = FP implementation

from misc import ioForPrinting


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
