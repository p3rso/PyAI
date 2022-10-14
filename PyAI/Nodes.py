def IONode(inp):
    if inp == 1:
        return(1)
    else:
        return(0)
def InvNode(inp):
    if inp == 1:
        return(0)
    else:
        return(1)
def CNode(inpa,inpb):
    if inpa + inpb == 2:
        return(1)
    if inpa + inpb == 1:
        return(1)
    if inpa + inpb == 0:
        return(0)
def XONode(inpa,inpb):
    if inpa + inpb != 2:
        return(1)
    else:
        return(0)
def NONode(inpa,inpb):
    if inpa + inpb != 1:
        return(1)
    else:
        return(0)

