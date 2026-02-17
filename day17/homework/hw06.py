# 6) შექმენით ინტეჯერების ლისტი, და ორი ცვლადი positive, negative. გამოიტანეთ სიაში არსებული დადებითი რიცხცების ჯამი, უარყოფითები რიცხვების რაოდენობა და დაპრინტე "zero" რამდენჯერაც შეგხვდება 0
numbers = [5, -3, 0, 7, -1, 0, 4, -6, 0]

positive_sum = 0
negative_count = 0

for num in numbers:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_count += 1
    else:
        print("zero")

print("დადებითი რიცხვების ჯამი:", positive_sum)
print("უარყოფითი რიცხვების რაოდენობა:", negative_count)
