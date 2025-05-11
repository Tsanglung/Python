h = float(input("身高(cm)：")) / 100
w = float(input("體重(kg)："))
bmi = round(w / (h * h), 3)  #  round 四捨五入到小數點三位
if bmi < 18:
    ans = "過輕"
elif bmi >= 18 and bmi <= 25:
    ans = "正常"
else:
    ans = "過重"
print(f" BMI ：{bmi}，{ans}")
