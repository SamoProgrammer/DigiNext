def SortText(text: str):
    deletes = 0
    currentCharacter = text[0]
    for i in range(1, len(text)):
        if text[i] == currentCharacter:
            deletes += 1
        else:
            currentCharacter = text[i]
    print(deletes)


userText = input()
SortText(userText)
