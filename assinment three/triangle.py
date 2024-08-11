
#check the triangle is equilateral,isosceles,scalene
a=int(input("Enter the lenght of a: "))
b=int(input("Enter the lenght of b: "))
c=int(input("Enter the lenght of c: "))
if a==b==c:
    print("Equilateral Triangle")
elif (a==b) or (a==c ) or (b==c):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")