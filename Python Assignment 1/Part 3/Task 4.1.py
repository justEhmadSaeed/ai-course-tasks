def isPalindrome(word):
    for i in range(0, int(len(word) / 2)):
        if (word[i] != word[len(word) - i - 1]):
            return False
    return True


word = input("Enter a word: ")

if isPalindrome(word):
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")