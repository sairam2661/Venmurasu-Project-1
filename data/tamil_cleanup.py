import re
lst = ['resources/Mahabharatha-Adiparva-Section22-ta.txt', 'resources/Mahabharatha-Adiparva-Section23-ta.txt', 'resources/Mahabharatha-Adiparva-Section24-ta.txt', 'resources/Mahabharatha-Adiparva-Section25-ta.txt', 'resources/Mahabharatha-Adiparva-Section26-ta.txt', 'resources/Mahabharatha-Adiparva-Section27-ta.txt', 'resources/Mahabharatha-Adiparva-Section28-ta.txt', 'resources/Mahabharatha-Adiparva-Section29-ta.txt', 'resources/Mahabharatha-Adiparva-Section30-ta.txt', 'resources/Mahabharatha-Adiparva-Section31-ta.txt']
file1 = open('data/final_tamil.txt', 'w', encoding='utf-8')
file1.close()
for file_name in lst:
  file = open(file_name, encoding='utf-8')
  string = ""
  for line in file:
      x = ''
      x = re.sub('\n', '', line)
      x = re.sub(''r"\([^()]*\)", "", x)
      x = re.sub(''r"\[[^()]*\]", "", x)
      x = re.sub(r'{.*?}', "", x, flags=re.UNICODE)
      x = re.sub('"', '', x)
      string += x
  string = " ".join(string.split())
  file1 = open('data/final_tamil.txt', 'a', encoding='utf-8')
  file1.write(string)
  file1.close()