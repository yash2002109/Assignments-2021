## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
## Code Here
for num in arr:
    if num%2==1:
        print(num)
        

'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here
for num in range(101):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)

'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here
print(string[::-1])
