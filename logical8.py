a=int(input("Enter the number of lines for pattern: "))

for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


# def counter(sentence):
#     words=sentence.split()
#     frequency={}
#     for i in words:
#         if i in frequency:
#             frequency[i]=frequency[i]+1
#         else:
#             frequency[i]=1
#     return frequency

# sentence="the cat and the dog"
# print(counter(sentence))