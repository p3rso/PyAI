FileN = open("Nodes.py")
exec(str(FileN.read()))
FileR = open("Random.py")
exec(str(FileR.read()))
inputamount = 10
Layers = 40 #recommended to be over 3 for best results
Networkingstr = []
ANetworkingstring = []
BNetworkingstring = []
CNetworkingstring = []
DNetworkingstring = []
ENetworkingstring = []
Ascore = 0
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
valA = 5
Position = 0
Multiplier = 0
Answer = []
Points = 0
Winner = []
Fin = 0
def Evolve(valA,inpstring):
    inpstring[(GenNumb(valA,1,(len(inpstring)-1)))] = str(GenNumb(valA+1,1,5))
    return(inpstring)
def AddLayer():      #ADD ONE TO VAL('LAYERS') WHEN CALLED!!!!!!(Not called by default!)
    while(addRounds <= inputamount):
        Networkingstr = Networkingstr + list(str(GenNumb(addRounds+1,1,5)))
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
    output = []
    while(roundse < inpamount):
        nodeinp = userinp[roundse]
        while(roundsf < layers):
            position = roundse + roundsf*inpamount
            nodeinp = UseNode(int(arryinp[position]),int(nodeinp),int(userinp[GenNumb((int(nodeinp)+1),int(0),int(1))]))
            roundsf = roundsf + 1
        output = output + list(str(nodeinp))
        roundsf = 0
        roundse = roundse + 1
    return(output)
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
    while(roundsg < inputamount - 1):
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
while(rounds <= Layers*inputamount-1):
    Networkingstr = Networkingstr + list(str(GenNumb(rounds+1,1,5)))
    rounds = rounds+1
    ANetworkingstr = CopyArray(Networkingstr)
    BNetworkingstr = CopyArray(Networkingstr)
    CNetworkingstr = CopyArray(Networkingstr)
    DNetworkingstr = CopyArray(Networkingstr)
    ENetworkingstr = CopyArray(Networkingstr)
ANetworkingstr = Evolve(valA,ANetworkingstr)
valA = valA+1
BNetworkingstr = Evolve(valA,BNetworkingstr)
valA = valA+1
CNetworkingstr = Evolve(valA,CNetworkingstr)
valA = valA+1
DNetworkingstr = Evolve(valA,DNetworkingstr)
valA = valA+1
ENetworkingstr = Evolve(valA,ENetworkingstr)
valA = valA+1
valA = 5
while(Fin == 0):
    roundsa = roundsa+1
    while(roundsc <= inputamount-1):
        Inp = Inp + str(input("Question: Input a bit:"))
        roundsc = roundsc + 1
    while(roundsd <= inputamount-1):
        Answer = Answer + list(str(input("Answer: Input a bit:")))
        roundsd = roundsd + 1
    Output = runarry(Networkingstr,Inp,inputamount,Layers)
    AOutput = runarry(ANetworkingstr,Inp,inputamount,Layers)
    BOutput = runarry(BNetworkingstr,Inp,inputamount,Layers)
    COutput = runarry(CNetworkingstr,Inp,inputamount,Layers)
    DOutput = runarry(DNetworkingstr,Inp,inputamount,Layers)
    EOutput = runarry(ENetworkingstr,Inp,inputamount,Layers)
    Soutput = str(score(Output,AOutput,BOutput,COutput,DOutput,EOutput,Answer))
    if Soutput == str("LAST"):
        print("The AI thought the answer was %s, it was %s" % (Output, Answer))
        Points = Points + 1
        Winner = Networkingstr
        Fin = int(input("This AI has completed %s Tests better than any other alteration, End simulation?(Y:1/N:0)" % Points))
    else:
        points = 0;
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
    ANetworkingstr = CopyArray(Networkingstr)
    BNetworkingstr = CopyArray(Networkingstr)
    CNetworkingstr = CopyArray(Networkingstr)
    DNetworkingstr = CopyArray(Networkingstr)
    ENetworkingstr = CopyArray(Networkingstr)
    ANetworkingstr = Evolve(valA,ANetworkingstr)
    valA = valA+1
    BNetworkingstr = Evolve(valA,BNetworkingstr)
    valA = valA+1
    CNetworkingstr = Evolve(valA,CNetworkingstr)
    valA = valA+1
    DNetworkingstr = Evolve(valA,DNetworkingstr)
    valA = valA+1
    ENetworkingstr = Evolve(valA,ENetworkingstr)
    valA = valA+1
    Inp = str("")
    Answer = []
    roundsc = 0
    roundsd = 0
print("Map of the Winner:%s" % Networkingstr)
