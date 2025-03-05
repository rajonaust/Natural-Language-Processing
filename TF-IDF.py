from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "apple orange apple banana",
    "apple mango banana",
    "banana mango"
]

vectorrizer = TfidfVectorizer()
tfidf = vectorrizer.fit_transform(documents)

matrix = tfidf.toarray()
voc = vectorrizer.get_feature_names_out()

for doc in range(len(documents)):
    print(documents[doc])
    for v in range(len(voc)):
        if matrix[doc][v] > 0:
            print(voc[v], ' = ', matrix[doc][v])
