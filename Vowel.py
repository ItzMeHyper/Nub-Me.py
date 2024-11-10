def check_vowel(ch):
    if(ch == "A" or ch == "a" or ch == "E" or ch == "e" or ch == "I" or ch == "i" or ch == "O" or ch == "o" or ch == "U" or ch == "u" ):
        print("The character is a vowel")
    else:
        print("The character is not a vowel")

char = input("Enter a character\n")
check_vowel(char)
