import math

print("1. 常數：pi 與 e")
print("圓周率 pi =", math.pi)
print("自然對數常數 e =", math.e)
print()

print("2. ceil(3.2)：無條件進位")
print(math.ceil(3.2))
print()

print("3. floor(3.8)：無條件捨去")
print(math.floor(3.8))
print()

print("4. copysign(-10, 5)：將 -10 轉為 +10")
print(math.copysign(-10, 5))
print()

print("5. fabs(-8.9)：浮點數絕對值")
print(math.fabs(-8.9))
print()

print("6. fmod(7, 3)：浮點數餘數")
print(math.fmod(7, 3))
print()

print("7. fsum([1.1, 2.2, 3.3])：浮點數總和")
print(math.fsum([1.1, 2.2, 3.3]))
print()

print("8. gcd(18, 24)：最大公約數")
print(math.gcd(18, 24))
print()

print("9. pow(2, 3)：2 的 3 次方")
print(math.pow(2, 3))
print()

print("10. sqrt(16)：平方根")
print(math.sqrt(16))
print()

print("11. factorial(5)：5 的階乘")
print(math.factorial(5))
print()

print("12. degrees(math.pi)：將弧度轉為角度")
print(math.degrees(math.pi))
print()

print("13. radians(180)：將角度轉為弧度")
print(math.radians(180))
print()

print("14. sin, cos, tan(math.pi/4)：弧度的三角函數")
print("sin:", math.sin(math.pi / 4))
print("cos:", math.cos(math.pi / 4))
print("tan:", math.tan(math.pi / 4))
print()

print("15. asin, acos, atan(1)：反三角函數")
print("asin:", math.asin(1))
print("acos:", math.acos(0))
print("atan:", math.atan(1))
print()

print("16. exp(1)：e 的 1 次方")
print(math.exp(1))
print()

print("17. log(10)：自然對數（以 e 為底）")
print(math.log(10))
print("log2(8)：以 2 為底")
print(math.log2(8))
print("log10(100)：以 10 為底")
print(math.log10(100))
print()

print("18. isclose(0.1+0.2, 0.3)：是否接近")
print(math.isclose(0.1 + 0.2, 0.3))
print()

print("19. isfinite, isinf")
print("math.isfinite(100):", math.isfinite(100))
print("math.isinf(float('inf')):", math.isinf(float("inf")))
print()

print("20. isnan(float('nan'))：是否為 NaN")
print(math.isnan(float("nan")))
