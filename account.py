# Pseudocode
# step 1. 
# Display option to user
    # 1. check, 2. withdraw, 3. deposite, 4. exit
# step 2. 
# if 1
    # Display balance
# elif 2
    # if balance is > the requested amount, subtract.
    # elif print 'not enough balance'
# elif 3
    # Add deposite to balance
    # print current balance
# elif 4
    # terminate options

balance = 0


print("\nChoose of the following options: ")
print("1. check ")
print("2. withdraw ")
print("3. deposite ")
print("4. exit ")

while True:
    check = input("your choice from 1-4:")


    if check == '1':
        print(f"your balance is {balance}")

    elif check == '2':
        withdraw = float(input("Enter withdrawal amount: "))
        if balance >= withdraw:
            balance -= withdraw
            print(f"You have successfully withdrawn {withdraw} amount. {balance} left in your account")
        else:
            print("Insufficient balance")
    elif check == '3':
        deposite = float(input("Enter deposite amount"))
        balance += deposite
        print(f"Your current balance now is {balance}")
    elif check == '4':
        print("Exiting the program")
        break
    else:
        print("Invalide choice.")