# misc.py = miscellaneous functions


def ioForPrinting(s:Optional[str])->str:
    """ format an input or output string for printing """
    specialChars = "->\"'\\,;?\n"
    if s==None:
        return "?"
    
    if s:
        containsSpecial = any(ch in specialChars for ch in s)
    else:    
        containsSpecial = True
    if containsSpecial:
        s = repr(s)
    return s    



#end
