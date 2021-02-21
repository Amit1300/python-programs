#count if string length is greater then 2 AND LAST AND FIRST char and number is same
def match_word(words):
    count=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count+=1
    print(count)
print(match_word(['aba','bbb','ddddddd']))
