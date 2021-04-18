import random
from datetime import datetime

database = {}

def init():
    
    print("Welcome to STAR Bank")

    have_account = int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))

    if(have_account == 1):
            login()

    elif(have_account == 2):
        open_account = int(input("Would you like to open an account with STAR Bank?: 1 (yes) 2 (no) \n"))
        if(open_account == 1):
            print(register())
            
        elif(open_account == 2):
             print("Thank you for your time!")
             exit()

    else:
        print("Wrong option selected")
        init()



def register():

    print(" ********* Thank you for choosing STAR Bank!, kindly input your details for an account opening.********** ")
    
    email = input("Enter your email address \n")
    first_name = input("Enter your first name \n")
    last_name = input("Enter your last name \n")
    password = input("Create your password \n")

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password, 0]



    print("Dear " + first_name + "," +  " " + "your account has been created successfully.")
    print(" ** ****** ******* ****** ** ")
    print("Your account number is: {}".format(account_number))
    print("Kindly ensure to keep it safe!")
    print(" ** ****** ******* ****** ** ")

    login()


def login():
    print(" ********** Welcome! input your account number and password to login ********** ")

    user_account_number = int(input("Enter your account number \n"))
    password = input("Enter your password \n")

    for account_number, user_details in database.items():
        if(account_number == user_account_number):
            if(user_details[3] == password):
                bank_operations(user_details)
 

        else:
            print("Invalid account number or password")
            login()




def bank_operations(user):
    print(" Welcome {} {}".format(user[0], user[1]))

    print(datetime.now())

    selected_option = int(input("What will you like to do?: (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

    if(selected_option == 1):
        deposit_operation()
    
    elif(selected_option == 2):
        withdrawal_operation()

    elif(selected_option == 3):
        login()
    
    elif(selected_option == 4):
        exit()
    
    else:
        print("Invalid option selected")
        bank_operations(user)

def deposit_operation():
    print(" ************ Deposit operations ************** ")
    #This are the things I want to do Nico
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance

    deposit = int(input('How much will you like to deposit? \n'))
    print(deposit)
    
    end_session = int(input("What will you like to do?: (1) Perform another transaction (2)exit"))

    if(end_session == 1):
        login()
    
    elif(end_session == 2):
        exit()

    else:
        print("you have selected a wrong option")


def withdrawal_operation():
    print(" ********** Withdrawal operations ************* ")
    #This are the things I want to do Nico
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance
    
    
    int(input('How much will you like to withdraw? \n'))
    print ('Please take your cash')
    end_session = int(input("What will you like to do?: (1) Perform another transaction (2)exit"))

    if(end_session == 1):
        login()
    
    elif(end_session == 2):
        exit_operation()

    else:
        print("you have selected a wrong option")

    

def logout_operation():
    login()

def exit_operation():
    exit()


def generate_account_number():
    
    return random.randrange(1111111111,9999999999)


def get_current_balance():
        for account_balance in database.items():
            print("Current account balance is {}".format(account_balance(4)))


init()
