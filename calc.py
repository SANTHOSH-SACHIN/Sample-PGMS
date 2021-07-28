import os
import math
def calc(n1,n2,op):
  if op == '1':
     print (n1,"+",n2,"=",n1+n2)
  elif op=='2':
     print (n1,"-",n2,"=",n1-n2)
  elif op=='3':
     print (n1,"*",n2,"=",n1*n2)
  elif op=='4':
     print (n1,"/",n2,"=",n1/n2)
  elif op=='5':
     print (n1,"%",n2,"=",n1%n2)
  elif op=='6':
     print (n1,"//",n2,"=",n1//n2)
  elif op=='7':
     print (n1,"power",n2,"=",n1**n2)
  elif op=='8':
     print ("sqrt of ",n1,"=",n1**0.5)
     print ("sqrt of ",n2,"=",n2**0.5)
  elif op=='9':
     print (n2,"th root of ",n1,"=",n1**(1/n2))
  elif op=='10':
     print ("log(",n1,")=",math.log(n1,10))
     print ("log(",n2,")=",math.log(n2,10))
yn = input("SHALL WE START THE CALCULATOR...y/n")
while (yn == ("y" or "Y" or 'y' or 'Y') ):     
    print( "SANTHOSH SACHIN\'S BINARY MATH CALCULATOR")
    num1=int(input("ENTER FIRST NUMBER : "))
    print("ENTER YOUR CHOICE OF BINARY OPERATION")
    print("1  :  ADD")
    print("2  :  SUBTRACT")
    print("3  :  MULTIPLY")
    print("4  :  DIVIDE")
    print("5  :  MODULO")
    print("6  :  FLOOR DIVIDE")
    print("7  :  POWER")
    print("8  :  SQUARE ROOT")
    print("9  :  NTH ROOT")
    print("10  :  LOG")
    operator= input()
    num2=int(input("ENTER SECOND NUMBER : "))
    calc(num1,num2,operator)
    yn = input("DO YOU WANT TO CONTINUE : y/n")
else:
    print ("THANK YOU FOR USING THE CALCULATOR") 