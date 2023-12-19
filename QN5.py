r=3
while(r==3):
    try:
        b=int(input("please enter five-digit integer:"))
        if(b>=10000 and b<100000):
            v=b//10000
            w=(b%10000)//1000
            x=(b%1000)//100
            y=(b%100)//10
            z=b%10
            sp=("   ")
            print(v,sp,w,sp,x,sp,y,sp,z)
        else:
            print("You entered wrong input,please try again")
    except ValueError:
        print("You entered wrong input,please try again")
        

