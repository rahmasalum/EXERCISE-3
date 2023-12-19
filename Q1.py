w=3
while(w==3):
    try:
        x=int(input("enter first integer:"))
        y=int(input("enter second integer:"))
        z=int(input("enter third integer:"))
        sum=x+y+z
        average=sum/3
        product=x*y*z
        smallest=min(x,y,z)
        largest=max(x,y,z)
        print("sum=",sum)
        print("averge=",average)
        print("product=",product)
        print("smallest=",smallest)
        print("largest=",largest)
    except ValueError:
        print(" nYou enter wrong input,please try again")
