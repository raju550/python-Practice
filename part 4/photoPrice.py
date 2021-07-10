print("Welcome to the rollstart")
height = int(input("what is your in cm? "))
if height >= 120:

    print("you can ride the rollercoaster")
    age = int(input("what is age? "))
    if age < 12:
        bill = 5
        print("please pay $5")
    elif age <= 18:
        bill = 7
        print("please pay $7")
    else:
        bill = 12
        print("please pay $12.")
    what_want = input("what is you want? Y or N")
    if what_want == "Y" or "y":
        bill += 3
    print(f"this is you ${bill}")
else:
    print("sorry, you have to grow taller before you")
