nums = [1, 2, 3]
nums.append(4)
print(nums)

nums = [1, 3, 5, 2, 4]
print(len(nums))

words = ["Python", "Fun"]
index = 1
words.insert(index, "is")
print(words)

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
#print(letters.index('z')) # 'z' is not in the index and results in error

# extra from bottom of List Function page (Solo Learn)
list = [1, 2, 3, 4, 1]
print(max(list))
print(min(list))
print(list.count(1))
list.remove(4)
print(list)
list.reverse()
print(list)