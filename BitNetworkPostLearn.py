FileN = open("Nodes.py")
exec(str(FileN.read()))
FileR = open("Random.py")
exec(str(FileR.read()))
LearnerOutput = ['3', '2', '1', '1', '5', '2', '2', '4', '1', '4', '3', '4', '3', '2', '4', '2', '4', '2', '5', '4', '2', '5', '1', '3', '1', '1', '1', '4', '1', '4', '2', '3', '2', '3', '4', '1', '5', '3', '3', '3', '5', '4', '1', '1', '3', '5', '3', '2', '2', '5', '3', '3', '3', '4', '4', '4', '3', '4', '4', '4', '5', '5', '5', '4', '4', '5', '4', '2', '1', '1', '5', '3', '4', '3', '3', '3', '3', '5', '3', '2', '2', '4', '2', '2', '4', '3', '4', '3', '2', '2', '3', '3', '3', '4', '2', '5', '5', '3', '3', '1', '4', '1', '1', '5', '3', '1', '1', '2', '4', '5', '5', '3', '4', '3', '4', '3', '3', '2', '2', '2', '3', '5', '3', '2', '5', '2', '4', '5', '4', '3', '2', '3', '2', '5', '3', '4', '2', '5', '2', '5', '1', '5', '1', '1', '3', '4', '3', '3', '4', '5', '4', '5', '5', '5', '5', '4', '3', '3', '2', '1', '4', '4', '5', '2', '2', '5', '1', '2', '1', '3', '1', '1', '4', '4', '4', '5', '3', '5', '2', '5', '5', '4', '4', '5', '5', '2', '2', '5', '2', '5', '5', '5', '2', '5', '1', '1', '3', '4', '4', '4', '4', '1', '2', '2', '2', '1', '3', '3', '3', '4', '5', '3', '3', '2', '5', '3', '2', '3', '5', '4', '5', '4', '3', '3', '4', '4', '5', '5', '4', '1', '3', '4', '4', '5', '3', '4', '5', '5', '3', '3', '3', '3', '4', '4', '2', '3', '2', '5', '3', '5', '1', '4', '2', '5', '5', '1', '3', '5', '4', '3', '2', '3', '5', '2', '2', '2', '4', '1', '3', '4', '4', '2', '5', '3', '3', '4', '2', '1', '2', '1', '3', '4', '2', '5', '2', '2', '5', '4', '5', '4', '1', '4', '4', '5', '3', '1', '3', '4', '4', '5', '5', '4', '3', '1', '3', '4', '5', '5', '4', '4', '2', '2', '4', '3', '4', '3', '5', '4', '2', '3', '2', '5', '1', '1', '5', '1', '2', '2', '2', '2', '5', '4', '4', '3', '5', '2', '3', '5', '2', '5', '2', '5', '3', '2', '4', '5', '5', '5', '3', '4', '3', '2', '1', '4', '3', '2', '5', '4', '4', '4', '2', '5', '5', '1', '5', '4', '2', '4', '4', '3', '4', '5', '3', '3', '2', '5', '4', '4', '2', '5', '4', '4', '4', '3', '5', '5', '2', '4', '2', '4', '3', '4', '2', '1', '2', '2', '2', '3', '5', '1']
Inputamount = 10
Layers = 40
AiOutput = []
roundsb = 0
roundsc = 0
Inp = ""
def UseNode(NodeType,Inpa,Inpb):
    if NodeType == 1:
        out = IONode(Inpa)
        return(out)
    if NodeType == 2:
        out = InvNode(Inpa)
        return(out)
    if NodeType == 3:
        out = CNode(Inpa,Inpb)
        return(out)
    if NodeType == 4:
        out = XONode(Inpa,Inpb)
        return(out)
    if NodeType == 5:
        out = NONode(Inpa,Inpb)
        return(out)
def runarry(arryinp,userinp,inpamount,layers):
    rounds = 0
    roundsa = 0
    nodeinp = 0
    output = []
    while(rounds < inpamount):
        nodeinp = userinp[rounds]
        while(roundsa < layers):
            position = rounds + roundsa*inpamount
            nodeinp = UseNode(int(arryinp[position]),int(nodeinp),int(userinp[GenNumb((int(nodeinp)+1),int(0),int(1))]))
            roundsa = roundsa + 1
        output = output + list(str(nodeinp))
        roundsa = 0
        rounds = rounds + 1
    return(output)
while(True):
    while(roundsb <= Inputamount-1):
        Inp = Inp + str(input("Question: Input a bit:"))
        roundsb = roundsb + 1
    AiOutput = runarry(LearnerOutput,Inp,Inputamount,Layers)
    while(roundsc <= Inputamount-1):
        print("AI Answer: Bit #%s: %s" % ((roundsc + 1),int(AiOutput[roundsc])))
        roundsc = roundsc + 1
    roundsb = 0;
    roundsc = 0;
    Inp = ""
