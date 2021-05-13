statesTable = [
    # q, T, ;, a1, 1, =, >, <, !
    [0, 0, 1, 2, 3, 4, 5, 6, 7],
    [1, 1, -1, -1, -1, -1, -1, -1, -1],
    [2, 1, -1,  2, 2, -1, -1, -1, -1],
    [3, 1, -1, -1, 3, -1, -1, -1, -1],
    [4, 1, -1, -1, -1, 8, -1, -1, -1],
    [5, 1, -1, -1, -1, 9, -1, -1, -1],
    [6, 1, -1, -1, -1, 10, -1, -1, -1],
    [7, 0, -1, -1, -1, 11, -1, -1, -1],
    [8, 1, -1, -1, -1, -1, -1, -1, -1],
    [9, 1, -1, -1, -1, -1, -1, -1, -1],
    [10, 1, -1, -1, -1, -1, -1, -1, -1],
    [11, 1, -1, -1, -1, -1, -1, -1, -1],
]

identifiers = ["<TERM>",
               "<var>",
               "<num>",
               "<eqTo>",
               "<GreatT>",
               "<LessT>",
               " ",
               "<EqualT>",
               "<GreEqT>",
               "<LesEqT>",
               "<DiffT>"]


class Lex:
    def __init__(self, value: str):
        self.value = value
        self.inputColumns = []
        self.res = []
        self.ident = []
        self.iterateString().iterateStates()

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
            currentState = statesTable[currentState][self.inputColumns[i]]
            id += self.value[i]

            if i == stringLen - 1:
                if statesTable[currentState][1] == 1:
                    self.res.append(id)
                    id = ""

                    self.ident.append(identifiers[currentState - 1])
                    currentState = 0

                else:
                    raise TypeError("\n\nInvalid symbol: '" +
                                    self.value[i] + "'")
            else:
                if statesTable[currentState][1] == 1 and (statesTable[currentState][self.inputColumns[i + 1]] < 0):
                    self.res.append(id)
                    id = ""

                    self.ident.append(identifiers[currentState - 1])
                    currentState = 0
        return self
