# -*- coding: utf-8 -*-
"""
@author: MikeTG (derived from acourso)
"""
from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.util import ngrams
import nltk
import re
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation

from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
"""
Test code below for CSV
"""
import csv


print()
print()
print()
print()
print('*************************************')
print('*************************************')

corpus_reader_cat2 = CategorizedPlaintextCorpusReader('./SpeechCorpus', r'.*\_.*\.txt',
                                                     cat_pattern=r'(\w+)/*')
##                                                   trump clinton speeches ##                                                   })
########## Various functions ##########
#strip punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def strip_punc(t):
    return ''.join(c for c in t if c.isalpha())
#######

print('****Categories List****')
print(corpus_reader_cat2.categories())
for category in corpus_reader_cat2.categories():
    print(category)
print()
print()
print()
print('****Documents by Categories Category****')
#print(corpus_reader_cat2.fileids('Clinton_2016'))
print(corpus_reader_cat2.fileids('Trump_2016'))
print()
print('*********hey********')
new_words = ['.',',',':>','<','>','?',"'",'-','--','...','"','."','$','>.','="'] ##added to mitigate the amount of unimportant words
stop_words = (stopwords.words('english') + new_words)
print(stop_words)
porter_stemmer = PorterStemmer()
word_net_lemmatizer = WordNetLemmatizer()

for fileids in corpus_reader_cat2.fileids('Trump_2016'): #all the documents under categorized folder
    print()
    print('the name',fileids)
    #print(corpus_reader_cat2.abspath(fileids)) #where the absolute pth on disk is
    #print(corpus_reader_cat2.paras(fileids)) #this prints out the entire document text in paragraph form
    content = [w for w in corpus_reader_cat2.words(fileids) if w.lower() not in stop_words]
    contentRaw = [w for w in corpus_reader_cat2.words(fileids) if w.lower() not in stop_words] #without lemmatizer or stem
    print("Raw", contentRaw)
    fdist2 = FreqDist(contentRaw)
    #nopunc = strip_punc(content)
    #print('remove punctuation',nopunc)
    print('Content: ', content)
    content = [porter_stemmer.stem(word) for word in content]
    print('Content_stemmer: ', content)
    content = [word_net_lemmatizer.lemmatize(word) for word in content]
    print("----")
    print(nltk.pos_tag(content))
    print('content final: ', content)
    fdist1 = FreqDist(content)
    print('frequency distribution', fdist1)
    print(fdist1.most_common(50))
    fdistcom = fdist1.most_common(50)
    bigrams = nltk.bigrams(content)
    trigrams = nltk.trigrams(content)
    quadgrams = ngrams(content, 4)

    freq_bi = nltk.FreqDist(bigrams)
    freq_tri = nltk.FreqDist(trigrams)
    freq_quad = nltk.FreqDist(quadgrams)

    the_test = freq_bi.most_common(20)
    the_tests = freq_tri.most_common(20)
    speechTag = nltk.pos_tag(content)

    print('brigrams',freq_bi.most_common(20))
    print('trigrams',freq_tri.most_common(20))
    print('quadgrams', freq_quad.most_common(20))

    #writing frequency distribution to file:
    # with open('test2.csv', 'a') as filehandle:
    #     for listitem in fdistcom:
    #         filehandle.write('{0} : {1}\n'.format(fileids,fdistcom))
    #
    # #writing bigrams to file:
    # with open('bigramsTest.csv', 'a') as filehandle2:
    #     for the_item in the_test:
    #         filehandle2.write('{0} : {1}\n'.format(fileids,the_test))

    #writing trigrams to file:
    with open('trigramsTest.csv', 'a') as filehandle3:
         for the_items in the_tests:
             filehandle3.write('{0} : {1}\n'.format(fileids,the_tests))

    #writing pos tagging to a file for further processing
    #this is much larger than i anticipated
    # with open('posTagTest.csv', 'a') as filehandle3:
    #     for the_items in speechTag:
    #         filehandle3.write('{0} : {1}\n'.format(fileids,speechTag))




'''
notes
20/06/04 - Must iterate over entire document via content, listed above.
....after initial run of code, only punctuation was occuring the most. Must address
....may want to remove stop words as i am not sure this is helping
...may want to include stemmers or remove. this is what's causing the dog versus dogs
...may be worth looking into time frame when 'lock her up' was first shown in my corpus. same with build the wall
...may set on stemmber, ignore stopwords = True
...ignore the punctuation



20/06/09
potentially use naive bayes to conduct a positive and negative count of words....need to determine tone of each speech just from positive versus negative?

20/06/16
Need to capture tagging of each corpus
Need to also look at homophilly...must look for news sources
Must find profiles of people in particular areas of interest
apply bag of words or frequency count
review tf_idf
need to do POS tagging ß

20/06/18
May want to look at negative words and see if they trend up, compare to previous election cycles

Review sentiment analysis
Perhaps do matching analysis against positive and negative words

20/06/24
Writing to the file is complete though it looks like the ngram analysis is not very useful as the time
'''
