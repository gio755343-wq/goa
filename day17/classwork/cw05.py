names = ["ანა", "ნიკა", "ანა", "გიორგი", "ანა"]

user_name = input("შეიყვანე სახელი: ")
count = 0

for name in names:
    if name == user_name:
        print("user name")
        count += 1
    else:
        print("not user name")

print(count)
