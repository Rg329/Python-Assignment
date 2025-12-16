a=open('Raghav.txt','r')
b=a.readlines()
print(b)
c=[]
for x in b:
    if x[-1] == '\n':
        c.append(x.strip())

print(c)
