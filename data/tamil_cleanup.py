import re
lst = ['Mahabharatha-Adiparva-Section22-ta.txt', 'Mahabharatha-Adiparva-Section23-ta.txt', 'Mahabharatha-Adiparva-Section24-ta.txt', 'Mahabharatha-Adiparva-Section25-ta.txt', 'Mahabharatha-Adiparva-Section26-ta.txt', 'Mahabharatha-Adiparva-Section27-ta.txt', 'Mahabharatha-Adiparva-Section28-ta.txt', 'Mahabharatha-Adiparva-Section29-ta.txt', 'Mahabharatha-Adiparva-Section30-ta.txt', 'Mahabharatha-Adiparva-Section31-ta.txt']
for file_name in lst:
  file = open(file_name, encoding='utf-8')
  string = ""
  for line in file:
      x = ''
      x = re.sub('\n', '', line)
      x = re.sub(''r"\([^()]*\)", "", x)
      x = re.sub(r'{.*?}', "", x, flags=re.UNICODE)
      x = re.sub('"', '', x)
      string += x
  string = " ".join(string.split())
  file1 = open('final_tamil.txt', 'a', encoding='utf-8')
  file1.write(string)
  file1.close()