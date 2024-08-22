print("-------Mini Calculator--------")
num1=float(input("Enter the first number:"))
num2=float(input("Enter the first number:"))
print("Press 1 for Addition \nPress 2 for Substraction \nPress 3 for Multiplication \nPress 4 for Division \n")
choice=int(input("Enter between 1-4\n "))
if choice==1:
    print("The addition of two number is:",num1+num2)
elif choice==2:
    print("The substraction of two number is:",num1-num2)
elif choice==3:
    print("The multiplicaton of two number is:",num1*num2)
elif choice==4 :
    print("The diviosion of two number is:",num1/num2)
else:
    print("Sorry invalid choice!!!!") 

    