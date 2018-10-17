def pigLatinConvert(text):
    # Assumes valid inputs consisting of only letters or numbers
    words = text.split(" ")
    pigLatin = ""
    for word in words:
        try:
            int(word)
            pigLatin += word + " "
            continue
        except:
            vowels = "aeiouy"
            if word[0].lower() in vowels:
                pigLatin += word + "yay "
                continue
            index = 0
            for letter in word:
                if letter.lower() in vowels:
                    pigLatin += word[index:] + word[0:index] + "ay "
                    break
                index += 1
    return pigLatin

text = ""
while text != "-1":
    text = input("What would you like to convert?: ")
    print(pigLatinConvert(text))