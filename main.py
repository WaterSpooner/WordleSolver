import string
def initDict():
    letterDict = {}
    for c in string.ascii_lowercase:
        letterDict[c] = 0
    return letterDict

def removeNonGreen(index, words, letter):
    newWords = []
    for word in words:
        if word[index] == letter:
            newWords.append(word)
    return newWords

def removeNonYellow(index, words, letter):
    newWords = []
    for word in words:
        if word[index] != letter and letter in word:
            newWords.append(word)
    return newWords
def removeBlackLetters(index,words, letter,ignoreLetters):
    newWords = []
    for word in words:
        if letter in ignoreLetters:
            if word[index] != letter:
                newWords.append(word)
        elif letter not in word:
            newWords.append(word)
    return newWords

def countLetters(words):
    letterDict = initDict()
    for word in words:
        for letter in word:
            letterDict[letter] +=1
    return letterDict

def wordScores(words,letterDict):
    scores = []
    for word in words:
        score = 0
        letters = initDict()
        for letter in word:
            if letters[letter] ==0:
                letters[letter] +=1
                score += letterDict[letter]
            else:
                letters[letter] +=1
                score += letterDict[letter]*(0.26/letters[letter])
        scores.append(score)
    return scores
def checkWord(guessedWord,finalWord):
    answer = []
    for x in range(0,5):
        if guessedWord[x] == finalWord[x]:
            answer.append("g")
        elif guessedWord[x] in finalWord:
            answer.append("y")
        else:
            answer.append("b")
    return answer


f = open("wordList.txt","r")
finalword = "witch"
lines = f.readlines()
words =[]
count = 0
letterIgnore = []
for line in lines:
    words.append(line.strip())
letterDict = countLetters(words)
wordScoreList = wordScores(words,letterDict)
wordsAndScores = list(zip(words,wordScoreList))
wordsAndScores.sort(key=lambda x: x[1],reverse=True)
while True:
    count+=1
    word = (wordsAndScores[0][0])
    if word == finalword:
        print("the word is " + word +" it took " + str(count) + " guess(es)")
        break
    print(word)
    blackRemove = []
    answer = checkWord(word,finalword)
    for x in range(0,5):
       #userinput = input("yellow,green or black (y,g,b)?")
        if answer[x] == "y":
            letterIgnore.append(word[x])
            words = removeNonYellow(x,words,word[x])
        elif  answer[x] == "g":
            letterIgnore.append(word[x])
            words = removeNonGreen(x,words,word[x])
        elif  answer[x] == "b":
            blackRemove.append(x)
    for i in blackRemove:
        words = removeBlackLetters(i,words,word[i],letterIgnore)

    letterDict = countLetters(words)
    wordScoreList = wordScores(words,letterDict)
    wordsAndScores = list(zip(words,wordScoreList))
    wordsAndScores.sort(key=lambda x: x[1],reverse=True)

