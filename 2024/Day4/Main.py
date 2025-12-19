f = open("D:\AoC2024\Day4\Sample0.txt", "r")
#f = open("D:\AoC2024\Day4\Sample0.txt", "r")
c = []

for a in f:
    print(a)
    c = a.find("XMAS")
    #for x in a:
        #print(x)

print(c)