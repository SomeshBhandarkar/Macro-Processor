import tables as t

#this is to check if the pointer is in macro code or the normal code which starts from START
mFlag = 0 
# to check if macro name is on the same line or on the next line    
mNameFlag = 0   

def OutWrite(token):
    Str1 = ' '.join(map(str,token))
    f = open("output.txt", "a")
    f.write(Str1+"\n")
    f.close()
    

def Start_Index_of_MDT(macroName):
    for i in range(0,len(t.MNT)):
        if (macroName == t.MNT[i][0]):
            return t.MNT[i][2]
    return 0


def Check_in_MNT(name): 
    for i in range(len(t.MNT)):
        if(name == t.MNT[i][0]):
            return True
    return False


def Replace_Arguments(token,Real_Arg,Element,Index):
    for i in range(len(token)):
        for j in range(len(Real_Arg)):
            if(token[i] == Element):
                token[i] = Real_Arg[Index - 1]
    return token


def instructionRecognizer(token):
    
    global mFlag,mNameFlag
    
    if (mFlag == 0):
        if (token[0] == 'MACRO'):
            mFlag = 1
            Macro_Processor(token)
        else:
            if(Check_in_MNT(token[0])):
                
                Real_Arguments = t.Replace_Arguments(token)
                
                i = Start_Index_of_MDT(token[0])
                
                while(i <= len(t.MDT)):
                    
                    if(t.MDT[i][0] == "MEND"):
                        break
                    
                    elif(Check_in_MNT(t.MDT[i][0])):
                        j = Start_Index_of_MDT(t.MDT[i][0])
                        while(j <= len(t.MDT)):
                            if(t.MDT[j][0] == "MEND"):
                                break
                            else:
                                OutWrite(t.MDT[j])
                            j += 1
                        
                    else:
                        temp = list()
                        for k in range(len(t.Arg_List)):
                            if(t.Arg_List[k][0] == token[0]):
                                temp = t.Arg_List[k]   

                        temp1 = list()
                        for k in range(len(t.MDT[i])):
                            for l in range(len(temp)):
                                if(t.MDT[i][k] == temp[l]):
                                    temp1 = Replace_Arguments(t.MDT[i], Real_Arguments, t.MDT[i][k], l)
                            
                        OutWrite(temp1)

                    i += 1
            else:
                OutWrite(token)
    else:
        Macro_Processor(token)

    
def Macro_Processor(token):
    
    global mFlag,mNameFlag
    
    if (token[0] == "MACRO"):
        if(len(token) > 1):
            Parameter = len(token) - 2
            t.addMNT(token[1],Parameter)
            t.addArgument(token, mNameFlag, token[1])
        else:
            mNameFlag = 1
    else:
        if (mNameFlag == 0):
            t.addMDT(token)
        else:
            Parameter = len(token) - 1
            t.addMNT(token[0],Parameter)
            t.addArgument(token,mNameFlag, token[0])
            mNameFlag = 0
        
    if (token[0] == "MEND"):
        mFlag = 0