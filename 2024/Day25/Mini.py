f = open("C:\\Users\\Geist\\Desktop\\AoC2024\\Day25\\Sample.txt", "r")
aInt = []
bInt = []
bData = []
iA = 0
iB = 0
iC = 0
iD = 0
iE = 0
iF = 0
curIndex = 0
bSave = False
zTtl = 0
maxS = 0
bCompatible = True

def process(ar1, ar2, bCompatible = True):
    #print('process')
    #print(ar1)
    #print(ar2)
    lar1 = ar1.split(',')
    lar2 = ar2.split(',')
    maxS = len(lar1) - 1
    pxS = int(lar1[maxS])
    #print(maxS)
    #print(pxS)
    for x in range(maxS):
        #print(lar1[x])
        iar1 = int(lar1[x])
        iar2 = int(lar2[x])
        if (iar1 + iar2) > pxS:
            if bCompatible == True:
                bCompatible = False
        else:
            print(f"Value {iar1} + {iar2}")
    #if bCompatible == True:
        #zTtl += 1
    #return zTtl
    return bCompatible

for a in f:
    #print(len(a))
    curIndex = 0

    if len(a) != 1:
        iF += 1
        for i in range(len(a)):
            rA = a[i]
            if rA == '#' and i == 0:
                bSave = False
            elif rA == '.' and i == 0:
                bSave = True

            if rA == '#':
                if curIndex == 0:
                    iA += 1
                elif curIndex == 1:
                    iB += 1
                elif curIndex == 2:
                    iC += 1
                elif curIndex == 3:
                    iD += 1
                elif curIndex == 4:
                    iE += 1
            curIndex += 1
    else:
        aStr = f"{iA},{iB},{iC},{iD},{iE},{iF}"
        if bSave == False:
            bInt.append(aStr)
        else:
            aInt.append(aStr)
        iA = 0
        iB = 0
        iC = 0
        iD = 0
        iE = 0
        iF = 0

#last Row
aStr = f"{iA},{iB},{iC},{iD},{iE},{iF}"
if bSave == False:
    aInt.append(aStr)
else:
    bInt.append(aStr)

print(aInt)
print(bInt)
#print(a)

#print(len(aInt))
#print(len(bInt))
xCnt = len(aInt)
yCnt = len(bInt)

if xCnt > yCnt:
    for x in aInt:
        for y in bInt:
            bCompatible = True
            bCompatible = process(x, y)
            if bCompatible == True:
                zTtl += 1
else:
    for x in bInt:
        for y in aInt:
            bCompatible = True
            bCompatible = process(x,y)
            if bCompatible == True:
                zTtl += 1

print(zTtl)