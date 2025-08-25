n = int(input())  # Number of words

for _ in range(n):
    word = input()  # Read each word
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)


