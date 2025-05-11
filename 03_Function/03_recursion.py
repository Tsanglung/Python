def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    return n


for i in range(10):
    print(fib(i), end=",")
print(end="\n")


def gcd(a, b):
    if a % b == 0:  # 如果相除餘數為 0，回傳結果
        return b
    else:  # 如果相除不為 0，表示還沒找到最大公因數
        return gcd(b, a % b)  # 使用遞迴，參數 a 使用 b，b 使用 a 除以 b 的餘數


print(gcd(36, 24))  # 12
