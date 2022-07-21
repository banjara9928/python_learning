file = open('demo.txt', 'r')
data = file.read()
data = file.readlines()
file.close()
print(data)


file = open('demo.txt', 'a')
file.write('This is a demo file')
file.writelines(['This is a demo file'])
file.close()
file.write('This is a demo file 2')
file.close()




def a (x):
    for i in range(0, len(x)):
        if x[1] in dct:
            dct[x[i]] +=1
        else:
            dct[x[i]] = 1
file=open('wikipidia.txt', 'r')
data = file.read()
x=data.split()
print(x)
dct={}
print(dct)           
print(max(dct))