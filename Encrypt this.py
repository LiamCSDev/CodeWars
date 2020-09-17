def encrypt_this(text):
    encryptedWord = []
    for word in text.split(): 
        lastWords = word[1:]
        if len(lastWords) > 1: 
            encryptedWord.append(str(ord(word[0])) + lastWords[-1:] + lastWords[1:-1] + lastWords[:1])
        else: 
            encryptedWord.append(str(ord(word[0])) + lastWords)
    return " ".join(encryptedWord)

print(encrypt_this("") == "")
print(encrypt_this("A wise old owl lived in an oak") == "65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
print(encrypt_this("The more he saw the less he spoke") == "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")
print(encrypt_this("The less he spoke the more he heard") == "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare")
print(encrypt_this("Why can we not all be like that wise old bird") == "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri")
print(encrypt_this("Thank you Piotr for all your help") == "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple")