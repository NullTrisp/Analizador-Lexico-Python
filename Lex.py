import LexData


class Lex:
    def __init__(self, value):
        self.value = value
        self.inputColumns = []
        self.res = []
        self.ident = []

    def getResult(self):
        return self.res

    def getIdent(self):
        return self.ident

    def iterateString(self):
        for char in self.value:
            asciiValue = ord(char)
            if char == ";":
                self.inputColumns.append(2)
            elif ((asciiValue >= 97) and (asciiValue <= 122)) or ((asciiValue >= 65) and (asciiValue <= 90)):
                self.inputColumns.append(3)
            elif ((asciiValue >= 48) and (asciiValue <= 57)):
                self.inputColumns.append(4)
            elif char == "=":
                self.inputColumns.append(5)
            elif char == ">":
                self.inputColumns.append(6)
            elif char == "<":
                self.inputColumns.append(7)
            elif char == "!":
                self.inputColumns.append(8)
            else:
                raise TypeError("\n\nInvalid symbol: '" + char + "'")
        return self

    def iterateStates(self):
        stringLen = len(self.value)
        currentState = 0
        id = ""
        for i in range(0, stringLen):
            currentState = LexData.statesTable[currentState][self.inputColumns[i]]
            id += self.value[i]

            if i == stringLen - 1:
                if LexData.statesTable[currentState][1] == 1:
                    self.res.append(id)
                    id = ""

                    self.ident.append(LexData.identifiers[currentState - 1])
                    currentState = 0

                else:
                    raise TypeError("\n\nInvalid symbol: '" +
                                    self.value[i] + "'")
            else:
                if LexData.statesTable[currentState][1] == 1 and (LexData.statesTable[currentState][self.inputColumns[i + 1]] < 0):
                    self.res.append(id)
                    id = ""

                    self.ident.append(LexData.identifiers[currentState - 1])
                    currentState = 0
        return self


try:
    lexer = Lex(input("Please input string to check: ")).iterateString().iterateStates()
    print(lexer.getResult(), lexer.getIdent())
except TypeError as err:
    print(err)
