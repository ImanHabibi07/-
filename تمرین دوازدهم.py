# ایمان حبیبی - 40419383
# برنامه ای برای کد عناوین کتاب بنویسید.
file = open("books.txt" , "r" )
x = len(file.readlines())
file.close()
i = 0
while i<x-1:
    file = open("books.txt" , "r")
    y = file.readlines()[i][0]
    file.close()
    file = open("books.txt" , "r")
    z = len(file.readlines()[i])
    file.close()
    print ( y , z-1 )
    i +=1
file = open("books.txt" , "r")
a = file.readlines()[x-1][0]
file.close()
file = open("books.txt" , "r")
b = len(file.readlines()[x-1])
print ( a , b )



