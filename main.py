#!/usr/bin/env pyhon3
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

# def get_cosine_sim(*strs): 
#     vectors = [t for t in get_vectors(*strs)]
#     return cosine_similarity(vectors)
    
# def get_vectors(*strs):
#     text = [t for t in strs]
#     vectorizer = CountVectorizer(text)
#     vectorizer.fit(text)
#     return vectorizer.transform(text).toarray()



if __name__ == '__main__':
    text1 = "This is a very interesting text"
    text2 = "This is another text, also very interesting"
    print("Jaccard: {}".format(get_jaccard_sim(text1,text2)))
#    print("Cosine:  {}".format(get_cosine_sim(text1,text2)))
    
          
