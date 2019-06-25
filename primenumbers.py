# given number is prime or not prime nuumber

num = int(input("enter the number:-"))

print("the number is:-",num)

if num > 1:
    for i in range(2,num):
        if (num % i)==0:
            print(num,"is not a prime ")

    else:
       print(num,"the number is prime")


else:
    print(num, "the number is not  prime number")
