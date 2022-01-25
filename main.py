print("\n-----------------------------------------------------")

#Write a Pyhton Program To Calculate the Factorial Of a List of Numbers

#input - 3 2 6

#output - 6 2 720

n=list(input("Enter The List = ").split(" "))
for i in n:
    fact=1
    for j in range(1,int(i)+1):
        fact=fact*j
    print("The Factorial OF ", n ,"is = ",fact)

print("\n-----------------------------------------------------")

#Display Prime Number Between M and N

#input 10 20
#output - 11 13 17 19

m,k=map(int,input("Enter 2 Nos = ").split())
p=[]
for i in range(m+1,k):
    flag=0
    for j in range(2,i//2+1):
        if((i%j)==0):
            flag=1
            break;
    if(flag==0):
        p.append(i)
print(p)


print("\n-----------------------------------------------------")