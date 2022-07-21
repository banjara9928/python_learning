try:
    print(5/'a')
except:
    print("you can't divide by zero")

                                    



y = lambda n: [i for i in range(n)]
print(y(5))

y=lambda x:[i*2 for i in range(x)]
print(y(5))