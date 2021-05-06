import LexLib

value = input("Please input string to check: ")


try:
    print(LexLib.iterateStates(LexLib.iterateString(value), value))

except TypeError as err:
    print(err)
