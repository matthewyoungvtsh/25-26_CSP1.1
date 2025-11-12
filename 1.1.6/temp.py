
y = 50
for x in range(1, 100):
    if x>y:
        print("success")
    if y>x:
        print("fail")

    if x + y > 10:
        print("blue")
    else:
        print("green")