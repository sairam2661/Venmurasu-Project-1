# Venmurasu Project

The project required solving two major tasks,

    1. Create a Tamil to English translation data set using the toy data given
    2. Evaluate the translation performance of existing open source models/services
For evaluating the translation performance, we used a metric called [BLEU score](https://cloud.google.com/translate/automl/docs/evaluate).


## Strategy 
The given tasks were solved using a sequential approach, where the work to be done was divided into five stages - three primary stages, and two additional stages.

## Stage 1 

In this stage, we preprocess the [toy data](https://github.com/sairam2661/Venmurasu-Project-1/tree/main/resources) using regex expressions in python as shown in `english_cleanup.py`, `tamil_cleanup.py` and obtain cleaned files in English and Tamil that are combined using `split_and_join.py` and stored in the [data](https://github.com/sairam2661/Venmurasu-Project-1/tree/main/data) folder.

## Stage 2 (Using IndicTrans)

In this stage, we translate the preprocessed and split [Tamil files](https://github.com/sairam2661/Venmurasu-Project-1/tree/main/translations/tamil) to [English files](https://github.com/sairam2661/Venmurasu-Project-1/tree/main/translations/english%20translated) using the [IndicTrans model](https://github.com/AI4Bharat/indicTrans#using-the-model-for-translating-any-input). This was done using python as shown in `translate.py`.

## Stage 3 (Using IndicTrans)

In this stage, the accuracy of the translations is measured. This was done, by calculating the [BLEU scores](https://cloud.google.com/translate/automl/docs/evaluate) by comparing the original English files present in `data` and the machine translated files obtained using the [IndicTrans model](https://github.com/AI4Bharat/indicTrans#using-the-model-for-translating-any-input) present in `translations`. 

The resultant **BLEU scores** were,

- Section 22 : 15.203970163533944
- Section 23 : 8.66774865115649
- Section 24 : 10.778457973213794
- Section 25 : 9.30828483646427
- Section 26 : 7.836188307965955
- Section 27 : 6.051237294940659
- Section 28 : 6.811132841838131
- Section 29 : 11.340100533389357
- Section 30 : 7.491865736701873
- Section 31 : 6.050756167829401

The overall **BLEU score** obtained was `8.9539742507034`.

## Stage 4 (Using GoogleTrans)

In this stage, we use other translation models available and evaluate their performance. We  decided to use the [GoogleTrans](https://py-googletrans.readthedocs.io/en/latest/) which is a library that implements the [Google Translate Ajax API](https://translate.google.com/). The files were translated using `translate-gt.py`, and were pushed to [translations-gt](https://github.com/sairam2661/Venmurasu-Project-1/tree/main/translations-gt). 

## Stage 5 (Using GoogleTrans)

In this stage, we compute the **BLEU scores** for the machine translated files obtained using this API. The program used to calculate the **BLEU scores**, `bleu_score_gt.py` are available in [evaluation-gt](https://github.com/sairam2661/Venmurasu-Project-1/tree/main/evaluation-gt). 

The resultant **BLEU scores** were,

- Section 22: 14.237897221624094
- Section 23: 9.044191474559641
- Section 24: 12.344096669167454
- Section 25: 10.66878638435959
- Section 26: 11.330478190561855
- Section 27: 8.203723702888546
- Section 28: 7.9148547626615855
- Section 29: 13.177553770766318
- Section 30: 8.34926222820818
- Section 31: 6.230928488448284

The overall **BLEU score** obtained was `10.150177289325`.

## Conclusion
In conclusion, the **BLEU scores** obtained were not as good as anticipated. This could be due to various factors such as,
1. Poor accuracy while translating proper nouns.
2. Splitting lines required manual supervision. 
3. Matching the English-Tamil pairs was difficult to implement automatically, due to the  difference in number of sentences present in English and Tamil sections.
4. The languages used were archaic, which could result in poor translation accuracy while implementing modern translation APIs.
5. The **BLEU scores** calculation algorithm demanded higher standards than to be expected of the Machine Translators.

From the **BLEU scores** calculated, the `IndicTrans API` was able to perform on par with `GoogleTranslate API`. 

## Team Members
1)Ashwin R
2)Bala Bharat Raaj GS 
3)Sairam Vaidya M
4)Gokula Krishnan S
5)Siva Bharathwaaj SS

