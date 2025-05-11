sum = (lambda x, y: x + y)(3, 5)
print(sum)

sum = lambda x, y: x + y
print(sum(3, 5))

loop = lambda n: [i for i in range(n)]  # 搭配 for迴圈
print(loop(10))

ifelse = lambda n: True if n < 1 else False  # 搭配判斷式
print(ifelse(-50))

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = map(lambda x: x**2, a)  # 搭配map
print(list(b))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
c = filter(lambda x: x > 4, a)  # 搭配 filter
print(list(c))  # [5, 6, 7, 8, 9]
