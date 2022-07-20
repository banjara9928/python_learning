
def greet():
    print("Hello, world!")
    return 'Hi Mars!'

 var = greet()
 print(var)    

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i 
        return fact


        return_of_5 = factorial(5)
        fact_of_10 = factorial(10)  

        print(fact_of_5)
        print(fact_of_10)



def table(n):
    for i in range(1,11):
      c=n*i
      
      print(c)

a=int(input())
table(a)    


def lst():
    return[4,5,6]
print(lst())



def a(n):
    if n.isupper():
        return True
    return False
n=input()
print(a(n))
    



def rb(n):
    a=0
    for i in n:
        c=ord(i)
        print(c)
        a+=c
    return a 
n=input()
print(rb(n))       
 


def sk(n):
    return sum(map(ord,n))
n=input()
print(sk(n))




def a(r,w):

    a=q[0:4]+w[-4:]
    return a
q=input()
w=input()
print(a(r,b))    



def a(w):
    n=len(w)

    for i in range(n):
        if ord(w(i+1)):
            sum+=1
            esle:i+1
            return sum_ 

            w = input()
            print(a(w))




def a(w):
    n=len(w)
    sum_=0
    for i in range(n-1):
        if (ord(i))+1==ord(w[i+1]):
            sum_+=1
    return sum_
w = input()
print(a(w)) 


def a(lst):
    for i in lst:
        if i%2==0_:
            print(i)
lst=[1,2,3,4,5,6,7,8,9]
print(a(lst))
