'''!pip install mosestokenizer
!pip install indic-nlp-library
!pip install sacrebleu
!pip install sacremoses'''

''' Program to compute the BLEU scores'''

import sacrebleu
from sacremoses import MosesDetokenizer

def calcBleuScore(fename, mtname):
    md = MosesDetokenizer(lang='en')

    # Open the test dataset human translation file and detokenize the references
    refs = []

    with open(fename) as test:
        for line in test: 
            line = line.strip().split() 
            line = md.detokenize(line) 
            refs.append(line)
        
    # print("Reference 1st sentence:", refs[0])

    refs = [refs]  # Yes, it is a list of list(s) as required by sacreBLEU

    # Open the translation file by the NMT model and detokenize the predictions
    preds = []

    with open(mtname) as pred:  
        for line in pred: 
            line = line.strip().split() 
            line = md.detokenize(line) 
            preds.append(line)

    # print("MTed 1st sentence:", preds[0])    

    # Calculate and print the BLEU score
    bleu = sacrebleu.corpus_bleu(preds, refs)
    print(bleu.score)

# Driver function
if __name__ == '__main__':
    fefiles = ["Mahabharatha-Adiparva-Section22-en final.txt", "Mahabharatha-Adiparva-Section23-en final.txt", "Mahabharatha-Adiparva-Section24-en final.txt", 
    "Mahabharatha-Adiparva-Section25-en final.txt", "Mahabharatha-Adiparva-Section26-en final.txt", "Mahabharatha-Adiparva-Section27-en final.txt", 
    "Mahabharatha-Adiparva-Section28-en final.txt", "Mahabharatha-Adiparva-Section29-en final.txt", "Mahabharatha-Adiparva-Section30-en final.txt", 
    "Mahabharatha-Adiparva-Section31-en final.txt"]
    MTefiles = ["Mahabharatha-Adiparva-Section22-en-MTGT.txt", "Mahabharatha-Adiparva-Section23-en-MTGT.txt", "Mahabharatha-Adiparva-Section24-en-MTGT.txt", 
    "Mahabharatha-Adiparva-Section25-en-MTGT.txt",  "Mahabharatha-Adiparva-Section26-en-MTGT.txt", "Mahabharatha-Adiparva-Section27-en-MTGT.txt", 
    "Mahabharatha-Adiparva-Section28-en-MTGT.txt", "Mahabharatha-Adiparva-Section29-en-MTGT.txt", "Mahabharatha-Adiparva-Section30-en-MTGT.txt", 
    "Mahabharatha-Adiparva-Section31-en-MTGT.txt"]  
    
    n = len(fefiles)

    # Calculating BLEU scores for the machine translated files (using GoogleTrans)
    for index in range(0, n):
        calcBleuScore(fefiles[index], MTefiles[index])