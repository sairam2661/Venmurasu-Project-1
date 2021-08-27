'''Program to split and join the cleaned English and Tamil files'''

'''This program was ineffective in splitting the sentences as required,
and produces poor results. So, the files were split locally using the commented
code, and were finally refined manually to maximise accuracy.'''

# The required files for Stage-1 were cleaned, combined and titled
# Mahabharata-Adiparva-Section-<Section Number>.txt
# using english_cleanup.py, tamil_cleanup.py and split_and_join.py


from mosestokenizer import *
from indicnlp.tokenize import sentence_tokenize

INDIC = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te"]

# Splitting sentences by using mosestokenizer

def split_sentences(paragraph, language):
    if language == "en":
        with MosesSentenceSplitter(language) as splitter:
            return splitter([paragraph])
    elif language in INDIC:
        return sentence_tokenize.sentence_split(paragraph, lang=language)

# Driver function

if __name__ == "__main__":
    #ffile = open('data/final_both.txt', mode='a', encoding='utf-8')
    
    tfile = open('data/final_tamil.txt', mode = 'r', encoding='utf-8')
    tamil = tfile.read()
    tsentences = split_sentences(tamil, language='ta')
    #tsentences = tamil.split(".")
    efile = open('data/final_english.txt', mode = 'r')
    english = efile.read()
    esentences = split_sentences(english, language='en')
    #esentences = efile.split(".")
    tfile.close()
    efile.close()

    #for sentence in range(0, min(len(tsentences), len(esentences)))):
    #   ffile.write(tsentences[sentence])
    #   ffile.write(esentences[sentence])
    #   ffile.write()

    #for sentence in range(len(tsentences)-len(esentences), len(tsentences)):
    #   ffile.write(tsentences[sentence])
    #   ffile.write()
    
    #ffile.close()    
