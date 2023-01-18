# 단어 input
N = int(input())
words = []
for i in range(N):
    words.append(input())

words_set = list(set(words)) #중복제거
words_set.sort() #사전순 정렬 후
words_set.sort(key = len) #길이로 정렬
for word in words_set:
    print(word)