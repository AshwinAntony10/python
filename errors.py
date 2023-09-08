try:
    num=int(input("enter a number:"))
    if num%2==o:
        print(f"{num}is even")
    else:
        print(f"{num}is odd" )
except ValueError:
    raise ValueError("invavlid input,please enter valid intiger.")
finally:
    print("hi")