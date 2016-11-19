import re

terminate = 0

while not terminate:
    
    try:
      print ("Syntax: Password must contain at least:")
      print ("  1 uppercase letter")
      print ("  1 lowercase letter")
      print ("  1 number, ")
      print ("  1 special character ($#!*&)")
      print ("  Minimum length = 8")
      passWord = input ('Enter password: ')
      # Perform syntax check
      length = len(passWord)
      numberTest = re.search(r'(.*?)[0-9]+', passWord)
      upperTest = re.search(r'(.*?)[A-Z]+', passWord)
      lowerTest = re.search(r'(.*?)[a-z]+', passWord)
      specialTest = re.search(r'(.*?)[$#@.!*&]+', passWord)
      verified = 0
      if length >= 8:
       if numberTest != None:
         if upperTest != None:
             if lowerTest != None:
                 if specialTest != None:
                   verified = 1
                  
      if (verified):
        print ("Password accepted!")
        terminate = 1
      else:
        raise ValueError
    except ValueError:
       print("*****Verificaton failed - try again*****")
