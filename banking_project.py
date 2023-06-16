print("*******"*20)
CustomerNames = ['James','David','John','Robert','Dora','Justin','Peter']
CustomerPins = ['1234', '4455', '6789', '7458', '2935','3024','5632']
Balances_of_Customers = [45000, 78624, 62400, 90000, 183004, 55870,25564]
deposition = 0
withdrawal = 0
balance = 0
count_1 = 1
count_2 = 5
i = 0

# This statement below helps the program to run continuously.
while True :
    print("_______"*20)
    print("\n")
    print("--------------------------------------------------------- Welcome to Grahmin Bank ---------------------------------------------------------- ")
    print("_______"*20)
    print("_______"*20)
    print("\n")
    
    print("     ----------   1.Open bank account          ----------  ")
    print("     ----------   2.Withdraw amount            ----------  ")
    print("     ----------   3.Deposit amount             ----------  ")
    print("     ----------   4.Check Customers & Balance  ----------  ")
    print("     ----------   5.Exit/Quit                  ----------  ")
    print("_______"*20)
    print("\n")
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
        print("Choice number 1 is selected by the customer")
        # The line below will take the no.of customers from the user.
        Num_of_Customers = eval(input("Number of Customers : "))
 
        i = i + Num_of_Customers
        # The if condition will restrict the number of new account to 5.
        if i > 5:
            print("\n")
            print("Customer registration exceeded or Customer registration too low")
            i = i - Num_of_Customers
        else:
            # The while loop will run according to the no. of customers.
            while count_1 <= i:
                # These few lines will take information from customer and then append them to the list.
                name = input("Enter Fullname : ")
                CustomerNames.append(name)
                pin = str(input("Please input a pin of your choice : "))
                CustomerPins.append(pin)
                balance = 0
                deposition = eval(input("Please input a value to deposit to start an account : "))
                balance = balance + deposition
                Balances_of_Customers.append(balance)
                print("Name=", end=" ")
                print(CustomerNames[count_2])
                print("Pin=", end=" ")
                print(CustomerPins[count_2])
                print("Balance=", end=" ")
                print(Balances_of_Customers, end=" ")
                print("Rs/-")
                count_1 = count_1 + 1
                count_2 = count_2 + 1
                print("Your name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("-----------------------------------------------------------New account created successfully !-------------------------------------------------")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(CustomerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("\n")
                print("*******************************************************************************************************************************************")
                # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        print("Choice number 2 is selected by the customer")
        # This while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            # This while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.
            while k < len(CustomerNames) - 1:
                k = k + 1
                # These two if conditions find where both the name and pin matches.
                if name == CustomerNames[k]:
                    if pin == CustomerPins[k]:
                        j = j + 1
                        # These few statement would show the balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(Balances_of_Customers[k], end=" ")
                        print("Rs/- \n")
                        balance = (Balances_of_Customers[k])
                        # Statement below would take the amount to withdraw from user.
                        withdrawal = eval(input("Input value to Withdraw : "))
                        # The if condition below would look whether the withdraw is greater than the balance.
                        if withdrawal > balance:
                            # This statement below would take a deposition from the customer.
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            # These few statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("Rs/- \n") 
                            balance = balance - withdrawal
                            print("-\n")
                            print("----------------------------------------------------------Withdrawal Successful!-----------------------------------------------------------")
                            Balances_of_Customers[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("Rs/- \n\n")
                        else:
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            balance = balance - withdrawal
                            # These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("----------------------------------------------------------Withdrawal Successful!-----------------------------------------------------------")
                            Balances_of_Customers[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("Rs/- \n\n")
            if j < 1:
                # The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        # The while loop below would work when the pin or the username is wrong.
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            # The while loop below will keep the function running to find the correct user.
            while k < len(CustomerNames)- 1:
                k = k + 1
                # The two if conditions below would find whether both the pin and the name is correct.
                if name == CustomerNames[k]:
                    if pin == CustomerPins[k]:
                        n = n + 1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(Balances_of_Customers[k], end=" ")
                        print("Rs/-")
                        balance = (Balances_of_Customers[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition
                        Balances_of_Customers[k] = balance
                        print("\n")
                        print("-----------------------------------------------------------Deposition successful!-----------------------------------------------------------")
                        print("Your New Balance: ", balance, end=" ")
                        print("Rs/- \n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        # The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(CustomerNames) - 1:
            print("->.Customer =", CustomerNames[k])
            print("->.Balance =", Balances_of_Customers[k], end=" ")
            print("Rs/-")
            print("\n")
            k = k + 1
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choiceNumber == "5":
        # These statements would be just showed to the customer.
        print("Choice number 5 is selected by the customer")
        print("\n")
        
        print("--------------------------------------------------Thanks for using Grahmin banking system!--------------------------------------------------")
        print("\n")
        print("Visit again")
        print("Have a Nice day!")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")