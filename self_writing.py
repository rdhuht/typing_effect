import time
import os

#phrase as a string
def write(phrase):
   list = [letter for letter in phrase] #create a list with the string
   strg = "" #the last pair of words
   pos = 0 #inicial index position
   
   for item in list:  
      strg = strg + list[0 + pos]
         
      time.sleep(0.1) #speed
      os.system("clear")
      print(strg)
         
      pos = pos + 1 #change the letter

if __name__ == "__main__":
   write("I like the typing effect") #type your phrase here
      
