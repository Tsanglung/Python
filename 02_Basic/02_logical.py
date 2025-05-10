a = 1
b = 100
if a > b:
    print("hello world !")
print("bye bye !")

if a < b:
    print("hello world !")
else:
    print("bye bye !")
print("ok.")

if a > b:
    print("a>b")
elif a < b:
    print("a<b")
else:
    print("a=b")
print("ok. down.")

c = a if a > b else b  # 三元運算簡化
print(c)


# 如果同時有 and 和 or，則會先判斷 and
c = 50
if a > b and a > c:
    d = a
elif a < c and b < c:
    d = c
elif a < b or a > c:
    d = b
else:
    pass
print(d)
