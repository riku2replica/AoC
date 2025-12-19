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
count = 0
locStr = []

def multiplier(x,y):
    return x * y

for a in f:
    #print(a)
    for b in range(len(a)):
        if(a[b] == 'm' or a[b] == 'M'):
            locStr.append(b)
            #print(count)
            #print('m found')
        #else:
            #print('no match ', {a[b]})
#print(locStr)

count = 0
strVal = ""
cumStr = []
for g in locStr:
    print(g)
    strVal = strVal + a[g]
    #print(a[g])
    print(strVal)
    count+=1
    if a[g] == ')':
        strVal += a[g]
        cumStr.append(strVal)
        count = 0
        break
    elif (a[g] == 'M' or a[g] == 'm') and count != 1:
        strVal += a[g]
        break
    else:
        strVal += a[g]
print(cumStr)

#Perform Second Layer?



