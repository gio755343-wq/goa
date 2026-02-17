# 4)შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს თავის გვარს, თუ პირველი 5 ასო შენი გვარის პირველი 5 ასოს მსგავსია, დაპრინტე 'almost same' სხვა შემთხვევაში დაპრინტე 'bye'
my_lastname = "katsiashvili" 

user_lastname = input("შემოიტანე შენი გვარი: ")

if user_lastname[:5] == my_lastname[:5]:
    print("almost same")
else:
    print("bye")
