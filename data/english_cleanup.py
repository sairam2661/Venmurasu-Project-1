import re

def cleanLine(line):
  if ('p. ' in line): 
    return ''
  if ('SECTION' in line):
    return ''
  else:
    x = ''
    x = re.sub('\n', '', line)
    x = re.sub(''r"\([^()]*\)", "", x)
    x = re.sub('"', '', x)
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
  lst1 = ['Mahabharatha-Adiparva-Section22-en.txt', 'Mahabharatha-Adiparva-Section23-en.txt', 'Mahabharatha-Adiparva-Section24-en.txt', 'Mahabharatha-Adiparva-Section25-en.txt', 'Mahabharatha-Adiparva-Section26-en.txt', 'Mahabharatha-Adiparva-Section27-en.txt', 'Mahabharatha-Adiparva-Section28-en.txt', 'Mahabharatha-Adiparva-Section29-en.txt', 'Mahabharatha-Adiparva-Section30-en.txt', 'Mahabharatha-Adiparva-Section31-en.txt']
  for file_name in lst1:
    file = open(file_name,'r')
    string = ""

    for line in file:  
      string += cleanLine(line)

    string = cleanPara(string)
    string = cleanApostrophe(string)
    file1 = open('final_english.txt', 'a')
    file1.write(string)
    file1.close()
    file.close()
  
  