def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n=int(input("enter no.:"))
print(f"factorial is:{factorial (n)}")
factorial(n)