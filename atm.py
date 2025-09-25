correct_pin = "1004"   
attempts = 3           
while attempts > 0:
    print("welcome to our ATM Mr NIJANTHAN")
    pin = input("Enter your 4-digit ATM PIN: ")
    input("Language Tamil or English:")
    if pin == correct_pin:
        print("PIN accepted. Access granted!")
        input("Transaction Current or Savings:")
        input("Deposite or Withdrawel:")
        input("Enter Your Amount:")
        print("Please Take Your Money and ATM Card")
        print("Thanks and Meet Again Have a Nice Day")
        break
    else:
        attempts -= 1
        print("Invalid PIN. Try again.")
        if attempts > 0:
            print(f"Remaining attempts: {attempts}")
        else:
            print("Card blocked due to too many invalid attempts.")
            
            print("Thanks and Meet Again!")


