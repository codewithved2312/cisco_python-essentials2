def checkanagrams(str1, str2):
    # remove spaces and convert to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    #compare  return 1 if true
    return sorted(str1) == sorted(str2)


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if checkanagrams(word1, word2):
    print(f'"{word1}" and "{word2}" are anagrams!')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')
