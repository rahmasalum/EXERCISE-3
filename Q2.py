m=6
while(m==6):
    try:
       r=int(input("please enter radius of a circle:"))
       d=2*r
       pie=3.14159
       c=2*pie*r
       a=pie*r**2
       print("diameter of a circle is:",d)
       print("circumference of a circle is:",c)
       print("area of a circle is:",a)
    except ValueError:
        print("You enter wrong input,please try again")

