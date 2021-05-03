import LexData


def iterateString(string):
    states = []

    for i in string:
        asciiValue = ord(i)

        if i == ";":
            states.append(3)
        elif ((asciiValue >= 97) and (asciiValue <= 122)) or ((asciiValue >= 65) and (asciiValue <= 90)):
            states.append(4)
        elif ((asciiValue >= 48) and (asciiValue <= 57)):
            states.append(5)
        elif i == "=":
            states.append(6)
        elif i == ">":
            states.append(7)
        elif i == "<":
            states.append(8)
        elif i == "!":
            states.append(9)
        else:
            raise TypeError("\n\n\nInvalid symbol: " + i)

    return states


def iterateStates(states, string):
    print(states)
    ident = []
    res = []
    currentState = 0
    id = ""
    for i in range(0, len(string)):
        currentState = LexData.tStates[currentState][states[i]]
        id = string[i]
        print(str(currentState) + " ", end="\0")

        if i == len(string):
            if LexData.tStates[currentState][1] == 1:
                res.append(id)

                if currentState == 1:
                    ident.append("<TERM>")
                elif currentState == 2:
                    ident.append("<var>")
                elif currentState == 3:
                    ident.append("<num>")
                elif currentState == 4:
                    ident.append("<eqTo>")
                elif currentState == 5:
                    ident.append("<GreatT>")
                elif currentState == 6:
                    ident.append("<LessT")
                elif currentState == 8:
                    ident.append("<EqualT>")
                elif currentState == 9:
                    ident.append("<GreEqT>")
                elif currentState == 10:
                    ident.append("<LesEqT>")
                elif currentState == 11:
                    ident.append("<DiffT>")

            else:
                raise TypeError("\n\n\nInvalid symbol: " + string[i])
        else:
            if LexData.tStates[currentState][1] == 1 and (LexData.tStates[currentState][states[i] - 1] < 0):
                res.append(id)
                if currentState == 1:
                    ident.append("<TERM>")
                elif currentState == 2:
                    ident.append("<var>")
                elif currentState == 3:
                    ident.append("<num>")
                elif currentState == 4:
                    ident.append("<eqTo>")
                elif currentState == 5:
                    ident.append("<GreatT>")
                elif currentState == 6:
                    ident.append("<LessT")
                elif currentState == 8:
                    ident.append("<EqualT>")
                elif currentState == 9:
                    ident.append("<GreEqT>")
                elif currentState == 10:
                    ident.append("<LesEqT>")
                elif currentState == 11:
                    ident.append("<DiffT>")
    return res, ident
