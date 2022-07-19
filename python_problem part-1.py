n = input('how many test cases: ')
n = int(n)

for i in range(n):
     op = input('please enter operation string: ')
     op_list = op.split()
     print(op_list)
    if op_list[0] == 'add':     
       first_number = int(op_list[1])
       second_number = int(op_list[2])
       print(first_number+second_number)
   elif op_list[0] == 'sub':
        


c=int(input())
b=0
for i in range(c):
    a=input().split()
    print(a)
    sum = 0
    if a[0] == 'add':
        for j in range(len(a)-1):
            b=int(a[j + 1])1
    
            sum+=b
            j+=1
            print(sum)       
        





 a= int(input())
 for i in range(1,a):
     a=a*i
print(a)


a= input("input a number")
b= input("enter another number")
a=int(a)
b=int(b)
operation= input("type the operation you want to perform: ")
if operation == "+":
  print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
      print(a*b)
elif operation == "/":
      print(a/b)
elif operation == "%":
      print(a%b)