try:
    pin = input("پین کد خود را وارد کنید: ")
    int(pin)
    print("پین کد ایجاد شد")
except ValueError:
    print("یک عدد را وارد کنید")