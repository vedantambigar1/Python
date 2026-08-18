score = float(input("enter the score between (0-100):"))
if score > 0 and  score <= 100:
    print("valid score")

if score >= 90:
    print("+A")

elif score >= 80:
    print("A")

elif score >= 70:
    print("B")

elif score >= 60:
    print("C")

elif score >= 55:
    print("D")

else:
    print("F")



