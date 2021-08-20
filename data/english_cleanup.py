import re

def cleanLine(line):
  if ('p. ' in line): 
    return ''
  else:
    x = ''
    x = re.sub('\n', '', line)
    return x

def cleanPara(string):
  return re.sub(r'^.*?"', '"', string)  

def cleanApostrophe(string):
   line = string.split()
   for ele in range(len(line)):
     if ("'" in line[ele]) and (',' in line[ele-1]):
       line[ele] = re.sub("'", '', line[ele])
     if ("'" in line[ele]) and ('!' in line[ele] or '?' in line[ele] or '.' in line[ele] or '!' in line[ele-1] or '?' in line[ele-1] or '.' in line[ele-1] or ']' in line[ele-1]):
       line[ele] = re.sub("'", '', line[ele])
   return " ".join(line)

if __name__ == "__main__":
  lst1 = ['resources/Mahabharatha-Adiparva-Section22-en.txt', 'resources/Mahabharatha-Adiparva-Section23-en.txt', 'resources/Mahabharatha-Adiparva-Section24-en.txt', 'resources/Mahabharatha-Adiparva-Section25-en.txt', 'resources/Mahabharatha-Adiparva-Section26-en.txt', 'resources/Mahabharatha-Adiparva-Section27-en.txt', 'resources/Mahabharatha-Adiparva-Section28-en.txt', 'resources/Mahabharatha-Adiparva-Section29-en.txt', 'resources/Mahabharatha-Adiparva-Section30-en.txt', 'resources/Mahabharatha-Adiparva-Section31-en.txt']
  file1 = open('data/final_english.txt', 'w')
  file1.close()
  for file_name in lst1:
    file = open(file_name,'r')
    string = ""

    for line in file:  
      string += cleanLine(line)

    string = cleanPara(string)
    string = cleanApostrophe(string)
    file1 = open('data/final_english.txt', 'a')
    file1.write(string)
    file1.close()
    file.close()
  print("success")
  
  