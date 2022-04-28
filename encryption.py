def encryptOn(string,encKey):
    encTextOn=""
    for char in string:
        if char.isalpha():
            if char.isupper():
                encTextOn+=chr((ord(char)+encKey-65)%26+65)
            else:
                encTextOn+=chr((ord(char)+encKey-97)%26+97)
        else:
            encTextOn+=char
    print("Tekst zaszyfrowany: "+encTextOn)
    
def encryptOff(string,encKey):
    encTextOff=""
    for char in string:
        if char.isalpha():
            if char.isupper():
                encTextOff+=chr((ord(char)-65)%26+65)
            else:
                encTextOff+=chr((ord(char)-97)%26+97)
        else:
            encTextOff+=char
    print("Tekst odszyfrowany: "+encTextOff)
    
encText=input("Tekst do szyfrowania:\n")
encKey=int(input("Klucz do szyfrowania:\n"))
encryptOn(encText,encKey)
encryptOff(encText,encKey)
