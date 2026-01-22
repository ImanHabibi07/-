# ایمان حبیبی - 40419383
# برنامه ای بنویسید که اسامی را در فایلی ایجاد کند.
file = open("names.txt" , "w")
names = ["John", "Oscar", "Jacob"]
file.write(names[0])
file.write("\n")
file.write(names[1])
file.write("\n")
file.write(names[2])
file.close()
file = open("names.txt" , "r")
print(file.read())
file.close()