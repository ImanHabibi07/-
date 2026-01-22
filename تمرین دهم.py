# ایمان حبیبی - 40419383
# بارفیکس
file = open("pull ups.txt")
n = int(input("روز مورد نظر را وارد کنید : "))
print ("Day" , n ,",",file.readlines()[n-1])
file.close()