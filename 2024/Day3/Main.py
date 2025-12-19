f = open("C:\\Users\\Geist\\Desktop\\AoC2024\\Day3\\Sample.txt","r")
bFlag = False
cumStr = []
bM = False
bU = False
bL = False
bOp = False
bCl = False
bNum = False
bComma = False

def multiplier(x,y):
    return x * y

def resetAll():
    bM = False
    bU = False
    bL = False
    bOp = False
    bCl = False
    bNum = False
    bComma = False

for a in f:
    #print(len(a))
    curStr = ''
    for b in range(len(a)):
        #print(a[b])
        if bM == False and a[b].upper == 'M':
            bM = True
        elif bU == False and a[b].upper == 'U':
            bU = True
        elif bL == False and a[b].upper == 'L':
            bL = True
        elif bOp == False and a[b] == "(":
            bOp = True
        elif bCl == False and a[b] == ")":
            bCl = True
        elif bComma == False and a[b] == ",":
            bComma = True
        elif bNum == False and (a[b] >= 0 or a[b] <= 9):
            bNum == True
        
        if (bM == True or bU == True or bL == True or bOp == True or bComma == True or bNum == True) and bCl == False:
            curStr += a[b]
            print(curStr)
            if bNum == True:
                bNum == False #reset
        elif(bCl == True):
            curStr += a[b]
            print(curStr)
            resetAll()
            cumStr.append(cumStr)
        else:
            resetAll()
            curStr = '' #clear