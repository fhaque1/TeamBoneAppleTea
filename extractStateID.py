def fileContentToList(filename):
    with open(filename) as file_:
        instream = file_.readlines()
    result = []
    for line in instream:
        result.append(eval(line.strip('\n,')))
    return result

def mapStateWithStateCode(dataList):
    dictResult = {}
    for line in dataList:
        dictResult[line[3]] = line[5]
    return dictResult

if __name__ == '__main__':
    dataList = fileContentToList('statesids')
    with open('stateCodeMap.txt', 'w') as file_:
        file_.write(str(mapStateWithStateCode(dataList)))
