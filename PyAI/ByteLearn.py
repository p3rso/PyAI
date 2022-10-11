FileN = open("Nodes.py")
exec(str(FileN.read()))
FileR = open("Random.py")
exec(str(FileR.read()))
FileS = open("Settings.txt")  #THESE FILES MUST BE IN THE SAME FOLDER AND DOWNLOADED. ERRORS WIL OCCUR OTHERWISE.
exec(str(FileS.read()))
Networkingstr = []
ANetworkingstring = []
BNetworkingstring = []
CNetworkingstring = []
DNetworkingstring = []
ENetworkingstring = []    #If you are reading this, you should only be here to run the AI or to edit the code.  User-Adjustable setings are available under "Settings.txt"
Ascore = 0                #If you are here to edit the code, Good luck!  I am terrible with comments and I dont really understand it either.  I just know it works. Have confidence, you got this!
Bscore = 0
Cscore = 0
Dscore = 0
Escore = 0
rounds = 0
roundsa = 0
roundsb = 0
roundsc = 0
roundsd = 0
addRounds = 0
skip = False
Output = []
AOutput = []
BOutput = []
COutput = []
DOutput = []
EOutput = []
Soutput = str("")
Inp = str("")
ByteInp = 0;
PreInp = str("")
valA = 5
Position = 0
Multiplier = 0
Answer = []
ByteAns = 0;
PreAns = str("")
Points = 0
Winner = []
bestwinner = []
bwinamt = 0
Fin = ""
lenarry = []
InputAmount = InputAmount * 8
def decodebin(inp,inplen):
    inp = int(inp)
    inputmap = ([" "] * inplen)
    rounds = 1
    roundsb = 0
    mapcount = 0
    number = 0
    byte = 0
    output = []
    outmap = []
    inpmap = list(str(inp))
    while(rounds < inplen):
        inputmap[rounds-1]  = int(inpmap[rounds-1])
        rounds = rounds + 1
    while(roundsb <= 8):
        MaxNumber = int((len(inputmap)/8)-1)
        if inputmap[(roundsb+(number*8))-1] == 1:
            byte = byte + 2^(8-roundsb)
        roundsb=roundsb+1
        if roundsb == 8:
            if number != MaxNumber:
                number = number + 1
                roundsb = 0
                output = output + [str(byte)]
                byte = 0
    output = output + [str(byte)]
    return(output)
def Evolve(valA,inpstring,times):
    x = 0;
    valB = valA
    while(x-1 < times):
        inpstring[(GenNumb(valB,1,(len(inpstring)-1)))] = str(GenNumb(valB+1,1,5))
        valB=valB+1
        x=x+1;
    return(inpstring)
def AddLayer():      #ADD ONE TO VAL('LAYERS') WHEN CALLED!!!!!!(Not called by default!)
    while(addRounds <= InputAmount):
        Networkingstr = Networkingstr + str(GenNumb(addRounds+1,1,5))
        addRounds = addRounds+1
        print("layer added!")
    return Networkingstr
def CopyArray(inp):
    out = []
    for val in inp:
        out.append(val)
    return out
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
def score(inp,inpa,inpb,inpc,inpd,inpe,ans):
    roundsg = 0
    scorelist = []
    TopScore = 0
    score = 0
    scorea = 0
    scoreb = 0
    scorec = 0
    scored = 0
    scoree = 0
    while(roundsg < (InputAmount/8) - 1):
        if ans[roundsg] == inp[roundsg]:
            score = score + 1
        if ans[roundsg] == inpa[roundsg]:
            scorea = scorea + 1
        if ans[roundsg] == inpb[roundsg]:
            scoreb = scoreb + 1
        if ans[roundsg] == inpc[roundsg]:
            scorec = scorec + 1
        if ans[roundsg] == inpd[roundsg]:
            scored = scored + 1
        if ans[roundsg] == inpe[roundsg]:
            scoree = scoree + 1
        roundsg = roundsg + 1
    scorelist = scorelist + list(str(score))
    scorelist = scorelist + list(str(scorea))
    scorelist = scorelist + list(str(scoreb))
    scorelist = scorelist + list(str(scorec))
    scorelist = scorelist + list(str(scored))
    scorelist = scorelist + list(str(scoree))
    scorelist.sort()
    TopScore = int(scorelist[len(scorelist)-1])
    if score == TopScore:
        return("LAST")
    if scorea == TopScore:
        return("A")
    if scoreb == TopScore:
        return("B")
    if scorec == TopScore:
        return("C")
    if scored == TopScore:
        return("D")
    if scoree == TopScore:
        return("E")
while(rounds <= Layers*InputAmount-1):
    Networkingstr = Networkingstr + list(str(GenNumb(rounds+1,1,5)))
    rounds = rounds+1
ANetworkingstr = CopyArray(Networkingstr)
BNetworkingstr = CopyArray(Networkingstr)
CNetworkingstr = CopyArray(Networkingstr)
DNetworkingstr = CopyArray(Networkingstr)
ENetworkingstr = CopyArray(Networkingstr)
ANetworkingstr = Evolve(valA,ANetworkingstr,Depth)
valA = GenNumb(valA+1,0,100)
BNetworkingstr = Evolve(valA,BNetworkingstr,Depth)
valA = GenNumb(valA+1,0,100)
CNetworkingstr = Evolve(valA,CNetworkingstr,Depth)
valA = GenNumb(valA+1,0,100)
DNetworkingstr = Evolve(valA,DNetworkingstr,Depth)
valA = GenNumb(valA+1,0,100)
ENetworkingstr = Evolve(valA,ENetworkingstr,Depth)
valA = GenNumb(valA+1,0,100)
valA = 5
while(Fin != "yes"):
    roundsa = roundsa+1
    while(roundsc <= (InputAmount/8)-1):  #mess with these two while loops if you are looking for program input not user input.
        ByteInp = min(255,int(input("Question: Input a byte:")))
        PreInp = str(bin(ByteInp))
        lenarry = lenarry + list(PreInp);
        PreInp = PreInp.removeprefix('0b')
        Inp = Inp + PreInp
        while(len(Inp) < ((roundsc+1)*8)):
            Inp = "0" + Inp
        roundsc = roundsc + 1
    while(roundsd <= (InputAmount/8)-1):
        Answer = Answer + [str(int(input("Answer: Input a byte:")))]
        roundsd = roundsd + 1
    Output = runarry(Networkingstr,Inp,InputAmount,Layers)
    AOutput = runarry(ANetworkingstr,Inp,InputAmount,Layers)
    BOutput = runarry(BNetworkingstr,Inp,InputAmount,Layers)
    COutput = runarry(CNetworkingstr,Inp,InputAmount,Layers)
    DOutput = runarry(DNetworkingstr,Inp,InputAmount,Layers)
    EOutput = runarry(ENetworkingstr,Inp,InputAmount,Layers)
    Soutput = str(score(Output,AOutput,BOutput,COutput,DOutput,EOutput,Answer))
    if Soutput == str("LAST"):
        print("The AI thought the answer was %s, it was %s" % (Output, Answer))
        Points = Points + 1
        Winner = Networkingstr
        Fin = str(input("This AI has completed %s Tests better than any other alteration, End simulation?(type 'yes' to stop)" % Points)) #mess with this to automate this program
    else:
        Points = 0
    if Soutput == str("A"):
        Winner = ANetworkingstr
        print("The AI thought the answer was %s, it was %s" % (AOutput, Answer))
    if Soutput == str("B"):
        Winner = BNetworkingstr
        print("The AI thought the answer was %s, it was %s" % (BOutput, Answer))
    if Soutput == str("C"):
        Winner = CNetworkingstr
        print("The AI thought the answer was %s, it was %s" % (COutput, Answer))
    if Soutput == str("D"):
        Winner = DNetworkingstr
        print("The AI thought the answer was %s, it was %s" % (DOutput, Answer))
    if Soutput == str("E"):
        Winner = ENetworkingstr
        print("The AI thought the answer was %s, it was %s" % (EOutput, Answer))
    Networkingstr = Winner
    if(Points > bwinamt):
        bwinamt = Points
        bestwinner = Winner
    ANetworkingstr = CopyArray(Networkingstr)
    BNetworkingstr = CopyArray(Networkingstr)
    CNetworkingstr = CopyArray(Networkingstr)
    DNetworkingstr = CopyArray(Networkingstr)
    ENetworkingstr = CopyArray(Networkingstr)
    ANetworkingstr = Evolve(valA,ANetworkingstr,Depth)
    valA = valA+1
    BNetworkingstr = Evolve(valA,BNetworkingstr,Depth)
    valA = valA+1
    CNetworkingstr = Evolve(valA,CNetworkingstr,Depth)
    valA = valA+1
    DNetworkingstr = Evolve(valA,DNetworkingstr,Depth)
    valA = valA+1
    ENetworkingstr = Evolve(valA,ENetworkingstr,Depth)
    valA = valA+1
    Inp = str("")
    Answer = []
    roundsc = 0
    roundsd = 0
print("Map of the Winner:%s" % Networkingstr)
print("Map of the best of all time:%s" % bestwinner)
