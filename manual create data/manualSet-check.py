if __name__ == '__main__':
    myFile = open("rawfile for find sen.txt",'r')
    #yixingFile = open()
    iMy = 0
    iYixing = 0
    iMyc = 0
    iMys = 0
    while True:
        mySentence = myFile.readline()
        if not mySentence:
            myFile.close()
            break;
        iMy = iMy + 1
        if mySentence.endswith("c\n") or mySentence.endswith("c\r\n"):
            mySentence = mySentence.split('\t')[0]
            mySentence = mySentence.split('`')
            if not (len(mySentence) == 1):
                print("sentence" + str(iMy) + " does not marked!!!")
        elif mySentence.endswith("s\n") or mySentence.endswith("s\r\n"):
            mySentence = mySentence.split('\t')[0]
            mySentence = mySentence.split('`')
            if not (len(mySentence) == 1):
                print("sentence" + str(iMy) + " is not pure sentence!!!")
        else:
            print("sentence" + str(iMy) + " has no end!!!")

