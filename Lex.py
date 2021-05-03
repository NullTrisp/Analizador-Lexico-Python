import LexLib

value = "aaa=as1>=22;;"  # input()

try:
    states = LexLib.iterateString(value)

    string, ident = LexLib.iterateStates(states, value)

    print()
    print(string, ident)

except TypeError as err:
    print(err)
