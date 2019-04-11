if __name__ == '__main__':
    id = open("id for post.txt",'r')
    SOURL = open("SOURL1001.txt",'w')
    i = 0
    while True:
        idLine = id.readline()
        if not idLine:
            id.close()
            break;
        idLine = idLine.split("\"")[1]
        i = i + 1
        if i >= 1001:
            SOURL.write("https://stackoverflow.com/questions/"+idLine+"\n")

    SOURL.close()