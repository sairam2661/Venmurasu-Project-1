from mosestokenizer import *
from indicnlp.tokenize import sentence_tokenize

INDIC = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te"]

def split_sentences(paragraph, language):
    if language == "en":
        with MosesSentenceSplitter(language) as splitter:
            return splitter([paragraph])
    elif language in INDIC:
        return sentence_tokenize.sentence_split(paragraph, lang=language)
        
if __name__ == "__main__":
    tfile = open('data/final_tamil.txt', mode = 'r', encoding='utf-8')
    tamil = tfile.read()
    #tsentence = split_sentences(tamil, language='ta')
    tsentence = tamil.split(".")
    print(len(tsentence))
    #for thing in tsentence:
    #    print(thing)
    efile = open('data/final_english.txt', mode = 'r')
    english = efile.read()
    #english = '"""' + english + '"""'
    esentences = english.split(".")
    print(len(esentences))
    #esentences = split_sentences(english, language='en')
    #print(len(esentences))
    tfile.close()
    efile.close()
    print("SUCCESSSS")
