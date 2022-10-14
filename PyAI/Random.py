def GenNumb(Rinp,floor,ceil):
    aout = Rinp/(Rinp**0.5)
    bout = aout*10000000
    cout = aout*100000
    cout = int(cout)
    cout = cout*100
    dout = bout - cout
    eout = Rinp+1/((Rinp)**0.5)
    fout = eout*10000000
    gout = eout*100000
    gout = int(gout)
    gout = gout*100
    hout = fout - gout
    if dout != 0:
        dout=(((ceil-floor)/100)*dout)
        dout=dout+(2*floor)
        return(int(dout))
    else:
        hout=(((ceil-floor)/100)*hout)
        hout=hout+(2*floor)
        return(int(hout))
