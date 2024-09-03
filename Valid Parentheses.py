s = "({[({{([()])}})]})" 
#s = "]" #Added this edge case 

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
        elif not Stack or Stack.pop() != pairs[i]: 
            return False
    return not Stack

print(main())
