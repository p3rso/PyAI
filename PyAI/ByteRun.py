FileN = open("Nodes.py")
exec(str(FileN.read()))
FileR = open("Random.py")
exec(str(FileR.read()))
FileS = open("Setings.txt")
exec(str(FileS.read())) #NOTE: ALL BELOW CODE *IS* INCLUDED IN "ByteLearn"!!!! (This is just easier for users/reformatted)
LearnerOutput = #paste output from "BitLearn" here! (printed to console, only if "Learn" Exited)
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
    roundse = 0
    roundsf = 0
    nodeinp = 0
    Nnodeinp = 0;
    Linp = 0
    output = []
    trueout = ""
    Preout = 0
    intout = []
    rounds = 0
    roundsa = 0
    while(roundse < inpamount-1):
        nodeinp = int(userinp[roundse])
        while(roundsf < layers):
            position = roundse + roundsf*inpamount
            Nnodeinp = UseNode(int(arryinp[position]),nodeinp,int(Linp))
            Linp = nodeinp
            nodeinp = Nnodeinp
            roundsf = roundsf + 1
        output = output + list(str(nodeinp))
        roundsf = 0
        roundse = roundse + 1
    while(len(trueout) < len(output)):
        trueout = trueout + output[rounds]
        rounds = rounds + 1
    intout = decodebin(trueout,InputAmount)
    print(intout)
    return(intout)
while(True):
    while(roundsb <= Inputamount-1):
        ByteInp = min(255,int(input("Question: Input a byte:")))
        PreInp = str(bin(ByteInp))
        lenarry = lenarry + list(PreInp);
        PreInp = PreInp.removeprefix('0b')
        Inp = Inp + PreInp
        while(len(Inp) < ((roundsc+1)*8)):
            Inp = "0" + Inp
        roundsb = roundsb + 1
    while(roundsd <= (InputAmount/8)-1):
        Answer = Answer + [str(int(input("Answer: Input a byte:")))]
        roundsc = roundsc + 1
    roundsb = 0;
    roundsc = 0;
    Inp = ""
