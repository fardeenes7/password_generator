#! /usr/bin/python3.8
import random

#Creating list for genaration

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special = ['!','@','#','$','%','^','&','*','(',')','-','=','[',']','{','}',';','|',':','<','>',',','.','?','/']
main = []

#Asking user what he wants

length = input("How long the password you want to be:")
l= input("Do you want to include letters(y/n):")
n = input("Do you want to include numbers(y/n):")
s = input("Do you want to include special characters(y/n):")

#adding everything into a single list whatever user wants
if l=='y' or l=='Y':
    main = main + letters
if n=='y' or n=='Y':
    main = main + numbers
if s=='y' or s=='Y':
    main = main + special

#Generating password

password = ''
for n in range(int(length)):
    password = password + random.choice(main)

print(password)