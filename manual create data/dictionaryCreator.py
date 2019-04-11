def inDict(dict, key):
    try:
        a = dict[key]
    except KeyError:
        return False, 0
    else:
        return True, a

if __name__ == '__main__':
    words = open("wordData.txt",'r', encoding='utf-8')
    wordsTrainSet = open("wordsTrainSet.txt",'w', encoding='utf-8')
    wordsTestSet = open("wordsTestSet.txt",'w', encoding='utf-8')
    total = 10966
    count = 0
    while True:
        line = words.readline()
        if not line:
            break;
        if count < total/10:
            wordsTestSet.write(line)
        else:
            wordsTrainSet.write(line)
        count = count + 1
        '''
        else:
            if inDict(dictionary, word)[1] != label:
                print("the word is " + word)
                print("previous label is " + label)
                print("another label is " + inDict(dictionary, word)[1])
                myJudge = input("judge it!")
                if myJudge != "c" and myJudge != "s":
                    myJudge = input("try again!")
                newline = {word: myJudge}
                dictionary.update(newline)

    for i in dictionary.items():
        print(i)
        '''