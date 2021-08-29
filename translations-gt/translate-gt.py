# pip install googletrans==3.1.0a0

from googletrans import Translator

# Implementing GoogleTrans library, (Google Ajax Translate API)
def translateGT(tafinal, gtfinal):
    translator = Translator()
    file1 = open("Mahabharatha-Adiparva-Section31-ta final.txt",'r',encoding='utf-8')
    file1_gt = open("Section31_gt.txt",'a',encoding='utf-8')
    while True:
        line = file1.readline()
        if not line:
            break
        print(line)
        line_gt = translator.translate(line,src='ta')
        print(line_gt.text)
        file1_gt.write(line_gt.text+'\n')
    file1.close()
    file1_gt.close()

# Driver function
if __name__ == '__main__':
    # List of tamil files, and required english Machine Translated files (using GoogleTrans)
    tfiles = ["Mahabharatha-Adiparva-Section22-ta final.txt", "Mahabharatha-Adiparva-Section23-ta final.txt", "Mahabharatha-Adiparva-Section24-ta final.txt", 
    "Mahabharatha-Adiparva-Section25-ta final.txt", "Mahabharatha-Adiparva-Section26-ta final.txt", "Mahabharatha-Adiparva-Section27-ta final.txt", 
    "Mahabharatha-Adiparva-Section28-ta final.txt", "Mahabharatha-Adiparva-Section29-ta final.txt", "Mahabharatha-Adiparva-Section30-ta final.txt", 
    "Mahabharatha-Adiparva-Section31-ta final.txt"]
    fefiles = ["Mahabharatha-Adiparva-Section22-en-MTGT.txt", "Mahabharatha-Adiparva-Section23-en-MTGT.txt", "Mahabharatha-Adiparva-Section24-en-MTGT.txt", 
    "Mahabharatha-Adiparva-Section25-en-MTGT.txt",  "Mahabharatha-Adiparva-Section26-en-MTGT.txt", "Mahabharatha-Adiparva-Section27-en-MTGT.txt", 
    "Mahabharatha-Adiparva-Section28-en-MTGT.txt", "Mahabharatha-Adiparva-Section29-en-MTGT.txt", "Mahabharatha-Adiparva-Section30-en-MTGT.txt", 
    "Mahabharatha-Adiparva-Section31-en-MTGT.txt"]
    
    n = len(tfiles)
    for index in range(0, n):
        translateGT(tfiles[index], fefiles[index])