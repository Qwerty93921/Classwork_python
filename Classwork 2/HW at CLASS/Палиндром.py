str = 'JaVaJ' 
str = str.casefold() 
 
# This string is reverse. 
rev = reversed(str) 
 
if list(str) == list(rev): 
   print("PALINDROME !") 
else: 
   print("NOT PALINDROME !") 





string=input(("Enter a letter:")) 
if(string==string[::-1]): 
      print("The letter is a palindrome") 
else: 
      print("The letter is not a palindrome") 




Num = int(input("Enter a value:")) 
Temp = num 
Rev = 0 
while(num > 0): 
    dig = num % 10 
    rev = rev * 10 + dig 
    num = num // 10 
if(Temp == rev): 
    print("This value is a palindrome number!") 
else: 
    print("This value is not a palindrome number!") 

# https://pythonpip.ru/examples/palindrom-na-python
