sample_data = "75,47,61,53,29"
rule = "75|47"
rule2 = "53|29"

a = rule.split("|")
b = rule2.split("|")

c = sample_data.split(",")
print(len(c))
print(len(a))
a1 = c.index(a[0])
a2 = c.index(a[1])
if(a1 < a2):
    print('Success 1')
else:
    print("Fail 1")
print(c.index(a[0]))
print(c.index(b[0]))
b1 = c.index(b[0])
b2 = c.index(b[1])
if(b1 < b2):
    print('Success 2')
else:
    print("Fail 2")