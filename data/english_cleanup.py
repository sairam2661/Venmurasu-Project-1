'''Program to cleanup English files'''

import re

# Function to clean all lines in the files

def cleanLine(line):
  if ('p. ' in line):   # Removing page numbers 
    return ''
  else:
    x = ''
    x = re.sub('\n', '', line)    # General cleaning
    return x

# Removing multiple spaces in final occurence

def cleanPara(string):
  return re.sub(r'^.*?"', '"', string)  

# Cleaning apostrophe's from paragraph

def cleanApostrophe(string):
   line = string.split()
   for ele in range(len(line)):
     if ("'" in line[ele]) and (',' in line[ele-1]):
       line[ele] = re.sub("'", '', line[ele])
     if ("'" in line[ele]) and ('!' in line[ele] or '?' in line[ele] or '.' in line[ele] or '!' in line[ele-1] or '?' in line[ele-1] or '.' in line[ele-1] or ']' in line[ele-1]):
       line[ele] = re.sub("'", '', line[ele])
   return " ".join(line)

# Driver function
if __name__ == "__main__":
  lst1 = ['resources/Mahabharatha-Adiparva-Section22-en.txt', 'resources/Mahabharatha-Adiparva-Section23-en.txt', 'resources/Mahabharatha-Adiparva-Section24-en.txt', 'resources/Mahabharatha-Adiparva-Section25-en.txt', 'resources/Mahabharatha-Adiparva-Section26-en.txt', 'resources/Mahabharatha-Adiparva-Section27-en.txt', 'resources/Mahabharatha-Adiparva-Section28-en.txt', 'resources/Mahabharatha-Adiparva-Section29-en.txt', 'resources/Mahabharatha-Adiparva-Section30-en.txt', 'resources/Mahabharatha-Adiparva-Section31-en.txt']
  
  fileFinal = open('data/final_english.txt', 'w')
  fileFinal.close()
  
  for file_name in lst1:
    file = open(file_name,'r')
    string = ""

    for line in file:  
      string += cleanLine(line)   # Cleaning line

    string = cleanPara(string)    # Cleaning paragraph
    string = cleanApostrophe(string)  # Cleaning apostrophe
    
    fileFinal = open('data/final_english.txt', 'a') 
    fileFinal.write(string) # Writing all lines to final_english.txt
    
    fileFinal.close()
    
    file.close()
  
  
  