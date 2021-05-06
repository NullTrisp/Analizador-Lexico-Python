import LexData


def iterateString(string):
    inputColumns = []
    for char in string:
        asciiValue = ord(char)
        if char == ";":
            inputColumns.append(2)
        elif ((asciiValue >= 97) and (asciiValue <= 122)) or ((asciiValue >= 65) and (asciiValue <= 90)):
            inputColumns.append(3)
        elif ((asciiValue >= 48) and (asciiValue <= 57)):
            inputColumns.append(4)
        elif char == "=":
            inputColumns.append(5)
        elif char == ">":
            inputColumns.append(6)
        elif char == "<":
            inputColumns.append(7)
        elif char == "!":
            inputColumns.append(8)
        else:
            raise TypeError("\n\nInvalid symbol: '" + char + "'")
    return inputColumns


def iterateStates(columns, string):
    stringLen = len(string)
    ident = []
    res = []
    currentState = 0
    id = ""
    for i in range(0, stringLen):
        currentState = LexData.statesTable[currentState][columns[i]]
        id += string[i]

        if i == stringLen - 1:
            if LexData.statesTable[currentState][1] == 1:
                res.append(id)
                id = ""

                ident.append(LexData.identifiers[currentState - 1])
                currentState = 0

            else:
                raise TypeError("\n\nInvalid symbol: '" + string[i] + "'")
        else:
            if LexData.statesTable[currentState][1] == 1 and (LexData.statesTable[currentState][columns[i + 1]] < 0):
                res.append(id)
                id = ""

                ident.append(LexData.identifiers[currentState - 1])
                currentState = 0

    return res, ident
