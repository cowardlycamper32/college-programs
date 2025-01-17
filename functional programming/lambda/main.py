data = [-10, 15, -20, 30, 0, -5, 8]
output = list(filter(lambda x: x < 0, data))
print(output)

data = ["dog", "cat", "elephant", "bat", "mouse", "ant"]
output = list(filter(lambda x: len(x) > 4, data))
print(output)

data = ["apple", "banana", "avocado", "cherry", "apricot"]
output = list(filter(lambda x: x[0].lower() == "a", data))
print(output)

data = [True, False, 1, 0, "hello", "", None]
output = list(filter(lambda x: not x, data))
print(output)

data = [0, 20, 30, 40]
output = list(map(lambda x: (x*(9/5))+32, data))
print(output)

data = ["apple", "banana", "cherry"]
output = list(map(lambda x: len(x), data))
print(output)

data = [1, 2, 3, 4, 5]
output = list(map((lambda x: x ** 2), data))
print(output)