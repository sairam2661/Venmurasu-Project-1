'''Program to cleanup Tamil files'''

import re

# Function to clean all lines in the files

def cleanLine(line):
  x = ''
  x = re.sub('\n', '', line)
  x = re.sub(''r"\([^()]*\)", "", x)
  x = re.sub(''r"\[[^()]*\]", "", x)
  x = re.sub(r'{.*?}', "", x, flags=re.UNICODE)
  x = re.sub('"', '', x)
  return x

# Driver function

if __name__ == '__main__':
  
  lst = ['resources/Mahabharatha-Adiparva-Section22-ta.txt', 'resources/Mahabharatha-Adiparva-Section23-ta.txt', 'resources/Mahabharatha-Adiparva-Section24-ta.txt', 'resources/Mahabharatha-Adiparva-Section25-ta.txt', 'resources/Mahabharatha-Adiparva-Section26-ta.txt', 'resources/Mahabharatha-Adiparva-Section27-ta.txt', 'resources/Mahabharatha-Adiparva-Section28-ta.txt', 'resources/Mahabharatha-Adiparva-Section29-ta.txt', 'resources/Mahabharatha-Adiparva-Section30-ta.txt', 'resources/Mahabharatha-Adiparva-Section31-ta.txt']
  
  fileFinal = open('data/final_tamil.txt', 'w', encoding='utf-8')
  fileFinal.close()
  
  for file_name in lst:
    file = open(file_name, encoding='utf-8')
    string = ""
    
    for line in file:
        x = cleanLine(line)
        string += x
    
    string = " ".join(string.split())
    
    fileFinal = open('data/final_tamil.txt', 'a', encoding='utf-8')
    fileFinal.write(string)
    
    fileFinal.close()
    