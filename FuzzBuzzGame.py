for x in range(101):
    if x % 3 == 0 :
        print("Fuzz")
    if x % 5 == 0:
        print("Buzz")
    if x % 3 == 0 and x % 5 == 0:
        print("FuzzBuzz")
    else:
        print(x)