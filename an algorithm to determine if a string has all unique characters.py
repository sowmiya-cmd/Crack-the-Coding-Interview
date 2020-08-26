def uniqueCharacters(str): 
  
    # Using sorting 
    sorted(str) 
  
    for i in range(len(str)-1): 
  
        # if at any time, 2 adjacent 
        # elements become equal, 
        # return false 
        if (str[i] == str[i + 1]) : 
            return False
              
    return True
  

str= input("enter your string:")
  
if (uniqueCharacters(str)) : 
    print("The String",str,"has all unique characters\n") 
      
else : 
        print("The String",str,"has duplicate characters\n") 
