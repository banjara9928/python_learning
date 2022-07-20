val=str.lower(input("Enter the word: "))
dic={}
for i in val:
    if  i in dic:
        dic[i]+=1
    else:
            dic[i]=1
            print(dic)





input=input("enter the number")
lst=[]
pop()
while True:
    commands = input()
    op, value = commands.split()
    if commands == 'stop':
        break
    elif commands == 'push':
        lst.append(value)

    elif commands == 'pop':
        index_of_value = lst.index(value)
        lst.pop(index_of_value)
    else:
        print('invalid command')
        continue    





while True:
    stud_info = input()
    
