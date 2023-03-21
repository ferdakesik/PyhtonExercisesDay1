#Exercise-1===> Cube Number Test... Print out all cubed numbers up to the total value 1000. 
# Meaning that if the cubed number is over 1000 break the loop.

for i in range(0,14):
    cube=i**3
    if cube>1000:
        break
    print("cube==>", cube)
print("cube is more than 1000==>",cube)

print()
#second way
print()

i=1
while True:
    cube=i**3
    if cube>1000:
        break
    print("cube==>",cube)
    i+=1
print("cube is more than 1000==>",cube)

#Exercise-2===>get prime numbers up to 1000
for num in range(1,1001):
    for i in range(2,(num+1)):
        if num%i==0:
           # print("This is not a prime number==>",num)
            break
        else:
            print("This is a prime number==>",num)
            break
        
#Exercise-3==>users input for their age, if they are younger than 18->kids
#if they are 18 to 65->adults ELSE print seniors

age=int(input("what is your age? "))
if age< 18:
    print("you are kid")
elif age>18 and age<65:
    print("you are adult")
else:
    print("you are senior")
    
    
            