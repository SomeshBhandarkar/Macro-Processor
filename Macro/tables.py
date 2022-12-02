MNT = list()             
MDT = list()               
Arg_List = list()     


def printMNT():
    for i in MNT:
        print(i)
        
def printMDT():
    for i in MDT:
        print(i)

def printArguments():
    for i in Arg_List:
        print(i)

def addMDT(token):
    MDT.append(token)

def addMNT(macro_Name,parameter):
    temp = list()
    temp.append(macro_Name)
    temp.append(parameter)
    
    Start_Index = len(MDT)
    
    temp.append(Start_Index)
    MNT.append(temp)

def addArgument(token,Flag,Name):
    temp = list()
    temp.append(Name)
    
    if(Flag == 0):
        for i in range(2,len(token)):
            temp.append(token[i])
        
        temp = [item.split('=') for item in temp]
        temp = [item for l in temp for item in l]
        
        Arg_List.append(temp)
        
    elif(Flag == 1):
        for i in range(1, len(token)):
            temp.append(token[i])
        Arg_List.append(temp)

        
def Replace_Arguments(token):
    Actual_Argument = list()
    for i in range(1,len(token)):
        Actual_Argument.append(token[i])
    
    return Actual_Argument