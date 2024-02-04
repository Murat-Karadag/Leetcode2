def mergeAlternately(word1: str, word2: str) -> str:

    limit = len(word1) + len(word2)

    runner = 0
    count1 = 0
    count2 = 0
    word = []

    while runner < limit:

        if len(word1) != count1:
            word.append(word1[count1])
            count1 += 1
            runner += 1


        if len(word2) != count2:
             word.append(word2[count2])
             count2 += 1
             runner += 1


        strword = "".join(word)

    return strword

str1 = "asa"
str2 = "gfbfbbfh"

print("Mixed Word:"+ mergeAlternately(str1, str2))