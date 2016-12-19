import urllib.request
# python module for retrieving url pages

# url with the vocabulary of interest
req = urllib.request.Request('https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt')
# open the url
response = urllib.request.urlopen(req)
# read the html file
the_page = response.read().decode("utf-8")

glossary = the_page.split()

for w in glossary:
    if '<pre' in w:
        start = glossary.index(w)
        # print(start)
    if'</pre' in w:
        finish = glossary.index(w)
        # print(finish)

narnia = glossary[start:finish]

# switch dict into list to delete useless stuffs and make all words into lowercases
listA = []   # initial list
listB = []   # 5 characters list
listC = []   # each word appears once only
listC2 = []  # values of each words
listD = []   # final list
for k in narnia:
    listA.append(k)
stringA = " ".join(listA)
stringA = stringA.replace(";","")
stringA = stringA.replace(":","")
stringA = stringA.replace(",","")
stringA = stringA.replace(".","")
stringA = stringA.replace("-","")
stringA = stringA.replace("'","")
stringA = stringA.replace('"',"")
stringA = stringA.replace("/","")
stringA = stringA.replace("(","")
stringA = stringA.replace(")","")
stringA = stringA.replace("_","")
stringA = stringA.replace("!","")
stringA = stringA.replace("?","")
stringA = stringA.lower()


# switch it back to dict and limit all words to 5 characters
listA = stringA.split()
for i in listA:
    if len(i) == 5:
        listB.append(i)

dictA = {}
for inst in listB:
    if inst not in dictA:
        dictA[inst] = 1
    else:
        dictA[inst] += 1
#print(dictA)

for k,v in dictA.items():
    listC.append(k)
    listC2.append(v)

#print(listC2)
