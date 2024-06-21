from func import *        # Function from Tong Sheng Kit (Non-registered customer)
from admin import *             # Function from Tan Zhong (Admin)
from cust import *         # Function from Wong Shi Zhou (Membership)
########  The main program start from here  ########

main_menu()
while True:  # This while loop is for continuously get option from user
    option = input("Please insert your option: ")                         # Press "5" to exit the program
    if option == "1":
        option1()
        get_option()

    elif option == "2":
        option2()
        get_option()

    elif option == "3":
        option3()
        get_option()

    elif option == "4":                       # Login page
        option4(admin, member)

    elif option == "5":               # Press "5" for program termination
        print("The program is exiting, Thank You!")
        break
    else:                                     # Error message when user give an input
        print("Incorrect option")             # that is not included in (1-5)

