FileN = open("Nodes.py")
exec(str(FileN.read()))
FileR = open("Random.py")
exec(str(FileR.read()))
FileS = open("Settings.txt")
exec(str(FileS.read())) #NOTE: ALL BELOW CODE *IS* INCLUDED IN "ByteLearn"!!!! (This is just easier for users/reformatted)
LearnerOutput =   #paste output from "BitLearn" here! (printed to console, only if "Learn" Exited)
AiOutput = []
roundsb = 0
roundsc = 0
Inp = ""
lenarry = []
InputAmount = InputAmount * 8
Answer = []
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
def decodebin(inp,inplen):
    inputmap = ([" "] * int(inplen))
    rounds = 0
    roundsb = 0
    mapcount = 0
    number = 0
    byte = 0
    output = []
    outmap = []
    while(rounds < inplen):
        inputmap[rounds]  = int(inp[rounds])
        rounds = rounds + 1
    while(roundsb < 8):
        MaxNumber = int((len(inputmap)/8)-1)
        if inputmap[(roundsb+(number*8))] == 1:
            byte = byte + ((2**(7-roundsb)))
        roundsb=roundsb+1
        if roundsb == 8:
            if number != MaxNumber:
                number = number + 1
                roundsb = 0
                output = output + [str(byte)]
                byte = 0
    output = output + [str(byte)]
    return(output)
def runarry(arryinp,userinp,inpamount,layers):
    roundse = 0
    roundsf = 0
    nodeinp = 0
    Nnodeinp = 0
    Linp = 0
    output = []
    trueout = ""
    Preout = 0
    intout = []
    rounds = 0
    roundsa = 0
    while(roundse < inpamount):
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
    if mode == "BYTE":
        intout = decodebin(output,InputAmount)
        return(intout)
    if mode == "BIN":
        return(output)
while(True):
    if mode == "BYTE":
        while(roundsb <= (InputAmount/8)-1):  #mess with these while loops if you are looking for program input not user input.
            ByteInp = min(255,int(input("Question: Input a byte:")))
            PreInp = str(bin(ByteInp))
            lenarry = lenarry + list(PreInp);
            PreInp = PreInp.removeprefix('0b')
            while(len(PreInp) < 8):
                PreInp = "0" + PreInp
            roundsb = roundsb + 1
            Inp = Inp + PreInp
    if mode == "BIN":
        while(roundsb <= InputAmount-1):
            Inp = Inp + str(min(1,int(input("Quetion: Input a bit:"))))
            roundsb = roundsb + 1
    if mode == "BYTE":
        while(roundsc <= (InputAmount/8)-1):
            Answer = Answer + [str(min(255,int(input("Answer: Input a byte:"))))]
            roundsc = roundsc + 1
    if mode == "BIN":
        while(roundsc <= InputAmount-1):
            Answer = Answer +[str(min(1,int(input("Answer:input a bit:"))))]
            roundsc = roundsc + 1
    Output = runarry(LearnerOutput,Inp,InputAmount,Layers)
    print("The AI thought the answer was %s, it was %s" % (Output, Answer))
    roundsb = 0;
    roundsc = 0;
    Inp = ""
