def ask():
    while True:
        try:
            rs = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print("Thank you, your number squared is: ")
            print(rs)
            break

ask()
