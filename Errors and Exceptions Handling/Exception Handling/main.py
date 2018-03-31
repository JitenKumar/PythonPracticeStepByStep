def ask_for_num():
    while True:
        try:
            res = int(input("Enter a number please"))
        except:
            print("That is not a number")
            continue
        else:
            print("Yes thank for that number")
            break
ask_for_num()