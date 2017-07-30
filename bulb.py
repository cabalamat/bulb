# bulb.py = FP implementation

import bbfuns


#---------------------------------------------------------------------

def main():
    for bbk in bbfuns.BB_CLASSES:
        bbf = bbk()
        print(bbf.getName())

#---------------------------------------------------------------------

if __name__=='__main__':
    main()

#end
