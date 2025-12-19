f = open("C:\\Users\\Geist\\Desktop\\AoC2024\\Day2\\Sample.txt","r")

decFlag = False
incFlag = False
failedFlag = False

first = ''
row = 0
sucFlag = 0

for a in f:
    b = a.split(' ')
    #print(row)
    row+=1
    first = ''
    decFlag = False
    incFlag = False
    failedFlag = False

    #print(b)
    for g in b:
        if first == '':
            first = int(g)
        else:
            if int(g) > first: #incremental
                if decFlag == False and incFlag == False:
                    incFlag = True
                elif decFlag == True:
                    if(failedFlag == False):
                        failedFlag = True
                
                if failedFlag == False:
                    gap = (int(g) - first)
                    if(gap > 3 and gap < 0):
                        failedFlag = True
            elif first > int(g):    #decrement
                if decFlag == False and incFlag == False:
                    decFlag = True
                elif incFlag == True:
                    if failedFlag == False:
                        failedFlag = True
                
                if failedFlag == False:
                    gap = (first - int(g))
                    if(gap > 3 and gap < 0):
                        failedFlag = True

    #if(decFlag):
        #print('decrease')
    #if(incFlag):
        #print('increase')
    #if(failedFlag == False):
        #sucFlag += 1
        #print('success')
        print(g)
        print(failedFlag)
print("Total Success Case : ", sucFlag)

