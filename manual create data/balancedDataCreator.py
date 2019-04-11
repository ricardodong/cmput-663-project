if __name__ == '__main__':
    newSenData = open("senData.txt", 'r')
    oldSenData = open("300linesSen.txt", 'r')
    senTrainSet = open("senTrainSet.txt",'w')
    senTestSet = open("senTestSet.txt", 'w')
    codeCount = 0
    senCount = 0
    # there are 399 inline code sentences and 401 pure sen in senData.txt
    while True:
        line = newSenData.readline()
        if not line:
            newSenData.close()
            break;
        senTrainSet.write(line)
        if line.endswith("c\n") or line.endswith("c"):
            codeCount = codeCount + 1
        else:
            senCount = senCount + 1
    print(codeCount, senCount)

    while True:
        line = oldSenData.readline()
        if not line:
            oldSenData.close()
            break;

        if line.endswith("c\n") or line.endswith("c"):
            if codeCount < 500:
                senTrainSet.write(line)
                codeCount = codeCount + 1
            else:
                senTestSet.write(line)
        else:
            if senCount < 500:
                senTrainSet.write(line)
                senCount = senCount + 1
            else:
                senTestSet.write(line)