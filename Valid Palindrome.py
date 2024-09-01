s = "({[({{([()])}})]})" 

pairs = {
    "]" : "[",
    ")" : "(",
    "}" : "{"
}

Stack = []

def main():
    for i in s:
        if i in pairs.values():
            Stack.append(i)
        elif not Stack or i in pairs:
            if pairs[i] == Stack[-1]:
                Stack.pop()
            else:
                return False
    return not Stack

print(main())