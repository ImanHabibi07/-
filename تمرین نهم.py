# ایمان حبیبی - 40419383
# برنامه ای برای سرو قهوه از یک دستگاه قهوه ساز بنویسید.
coffee = ["کافه لاته", "کافه آمریکانو", "اسپرسو", "کاپوچینو", "ماکیاتو"]
try:
    x = int(input("یک عدد بین 0 تا 4 انتخاب کنید: "))
    if 0 <= x <= 4:
        print(coffee[x])
    else :
        print ( "invalid number")
except ValueError:
    print("invalid number")
finally:
    print("have good day")