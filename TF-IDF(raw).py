import math

documents = [
    "apple orange apple banana",
    "apple mango banana",
    "banana mango"
]

def TF(w, doc):
    words = doc.split()
    cnt = 0
    for wr in words:
        if w == wr:
            cnt = cnt + 1
    return cnt / len(words)

def IDF(w, corpus):
    cnt = 0 
    for doc in corpus:
        if w in doc.split():
            cnt = cnt + 1
    return math.log(len(corpus)/cnt + 1)

def TF_IDF(w, doc, corpus):
    return TF(w, doc) * IDF(w, corpus)    

for d in range(len(documents)):
    print(documents[d])
    for w in set(documents[d].split()):
        print(w, '=', TF_IDF(w, documents[d], documents))