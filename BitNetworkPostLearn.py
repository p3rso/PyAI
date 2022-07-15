FileN = open("Nodes.py")
exec(str(FileN.read()))
FileR = open("Random.py")
exec(str(FileR.read())) #NOTE: ALL BELOW CODE *IS* INCLUDED IN "BitLearn"!!!! (This is just easier for users/reformatted)
LearnerOutput = #paste output from "BitLearn" here! (printed to console)
Inputamount = 10 #must be the same as the var in "BitLearn"
Layers = 40 #must be the same as the var in "BitLearn"
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
