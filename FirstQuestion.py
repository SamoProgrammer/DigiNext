def TextExtender(text: str, n: int):
    result = ""
    aCount = 0
    textLength = len(text)
    quotient = int(n/textLength)
    remaining = n % textLength
    for i in range(0, quotient):
        result += text
    for b in range(0, remaining):
        result += text[b]
    for x in result:
        if x == "a":
            aCount += 1
    print(aCount)


userText = input()
userNewLength = input()
TextExtender(userText, int(userNewLength))
