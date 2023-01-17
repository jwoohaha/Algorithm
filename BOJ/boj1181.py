#  단어 정렬
#  길이가 짧은 것부터
#  길이가 같으면 사전 순으로

# 단어 input
N = int(input())
words = []
for i in range(N):
    words.append(input())

words_set = list(set(words))  # 중복제거
words_set.sort()  # 사전순 정렬 후
words_set.sort(key=len)  # 길이로 정렬
for word in words_set:
    print(word)
