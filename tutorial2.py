num = int(input("please input a number that is a multiple of 2,3,4: "))
while num<=0:
    num = int(input("please input a positive number: "))

if num %2 ==0 or num %3 ==0 or num%4 ==0:
    print("the number",num,"is the multiple of 2,3,4")
else:
    print("the number",num,"is not multiple of 2,3,4")
print("End of program")