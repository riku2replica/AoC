f = open("D:\AoC2024\Day5\Sample.txt", "r")
#f = open("D:\AoC2024\Day5\Full.txt", "r")
s1 = ""
s2 = ""
lIndex = []
rIndex = []
Section2 = []


for a in f:
    #print(a)
    if a.count("|") > 0:
        b = a.split("|")
        #print("section 1")
        lIndex.append(b[0])
        rIndex.append(b[1].replace("\n",""))
    elif a.count(",") > 0:
        #print("section 2")
        #c = a.split(",")
        s1 = a.replace("\n","")
        Section2.append(s1)
    #for x in a:
        #print(x)
#print(lIndex)
#print(len(lIndex))
#print(len(rIndex))
#print(Section2)

bTest = True


curIndex = 0
bProceed = True
bReset = False
bPass = False
TtlMid = 0
sectSplit = []
print(len(lIndex))

if bTest == True:
    while bProceed:
        for sect in Section2:
            curIndex = 0
            sect = sect.replace("\n","")
            print(sect)
            sectSplit = sect.split(',')
            if curIndex < len(lIndex):
                print(lIndex[curIndex])
                try:
                    a1 = sectSplit.index(lIndex[curIndex])
                except:
                    a1 = 0
                
                try:
                    b1 = sectSplit.index(rIndex[curIndex])
                except:
                    b1 = 0

                print(a1)
                print(b1)
                #print(rIndex[curIndex])
                if a1 < b1:
                    print('before')
                else:
                    print('after')
                curIndex+=1
            else:
                if (bProceed == True):
                    bProceed = False
                #print('else')