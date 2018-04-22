words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1 # max_index = 3

while counter <= max_index: # counter (0) less than or equal to max_index (3)
    word = words[counter]
    print(word + "!")
    counter = counter + 1

words = ["hello", "world", "spam", "eggs"]
print(word)
for word in words:
    print(word + "!")

for i in range(5):
    print("hello!")