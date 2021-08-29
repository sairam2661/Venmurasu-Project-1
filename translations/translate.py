# install these libraries
# pip install indic-nlp-library

'''Program to translate the cleaned Tamil sentences into English'''

from indicnlp import *

# Function to translate the files
def translMTenfiles(tname, ename):
    mtenfile = open(ename,'w',encoding='utf-8')
    mtenfile.close()
    tfile = open(tname,'r',encoding='utf-8')
    mtenfile = open(ename,'a',encoding='utf-8')
    #print('Get current working directory :      ', os.getcwd())
    #s = tfile.readline()
    # Translating the lines into a new file stored in ename
    while True:
        line = tfile.readline()
        if not line:
            break
        #print("Line{}: {}".format(count, line.strip()))
        print(line)
        linet=indic2en_model.translate_paragraph(line, 'ta', 'en')
        print(linet)
        mtenfile.write(linet + '\n')

# Driver function
if __name__ == '__main__':
    # List of tamil files, and required english MT files
    tfiles = ["Mahabharatha-Adiparva-Section22-ta final.txt", "Mahabharatha-Adiparva-Section23-ta final.txt", "Mahabharatha-Adiparva-Section24-ta final.txt", 
    "Mahabharatha-Adiparva-Section25-ta final.txt", "Mahabharatha-Adiparva-Section26-ta final.txt", "Mahabharatha-Adiparva-Section27-ta final.txt", 
    "Mahabharatha-Adiparva-Section28-ta final.txt", "Mahabharatha-Adiparva-Section29-ta final.txt", "Mahabharatha-Adiparva-Section30-ta final.txt", 
    "Mahabharatha-Adiparva-Section31-ta final.txt"]
    fefiles = ["Mahabharatha-Adiparva-Section22-en-MT.txt", "Mahabharatha-Adiparva-Section23-en-MT.txt", "Mahabharatha-Adiparva-Section24-en-MT.txt", 
    "Mahabharatha-Adiparva-Section25-en-MT.txt",  "Mahabharatha-Adiparva-Section26-en-MT.txt", "Mahabharatha-Adiparva-Section27-en-MT.txt", 
    "Mahabharatha-Adiparva-Section28-en-MT.txt", "Mahabharatha-Adiparva-Section29-en-MT.txt", "Mahabharatha-Adiparva-Section30-en-MT.txt", 
    "Mahabharatha-Adiparva-Section31-en-MT.txt"]
    
    n = len(tfiles)
    for index in range(0, n):
        translMTenfiles(tfiles[index], fefiles[index])


