from datetime import datetime
import operation
import read
import write

today_date_and_time = datetime.now()

def Welcome():
    """
    Welcome message and main interaction loop for the user.
    """
    while True:
        print("\n")
        print("****************************************************************************************************************")
        print("*******************************-- WELCOME TO TECHNOPROPERTY NEPAL --********************************************")
        print("*********************************-- YOUR ONE-STOP RENTAL SOLUTION --********************************************")
        print("*                                                                                                              *")
        print("*                                     Address: Kathmandu, Nepal                                                *")
        print("*                                          Phone: 01-2345678                                                   *")
        print("*                                     Email: info@technonepal.com                                              *")
        print("****************************************************************************************************************")
        print("\n")
        print("                                  Lands available in Our Company  ")
        print("****************************************************************************************************************")
        print("       Kitta No       City/DistrictName       Direction          Anna            Price        Availability Status")
        print("****************************************************************************************************************")
        read.Rent_details()

        try:
            user_choice = input("Do you want to rent a land, return a land, or exit? (rent/return/exit): ").lower()
            if user_choice == 'rent':
                while True:
                    try:
                        kitta_number = int(input("Enter the Kitta Number you want to rent: "))
                        operation.interact_land(str(kitta_number), 'rent')
                        ask_for_more('rent')
                        break
                    except ValueError:
                        print("Error: Please enter a valid numeric Kitta Number.")
                        continue

            elif user_choice == 'return':
                while True:
                    try:
                        kitta_number = int(input("Enter the Kitta Number you want to return: "))
                        operation.interact_land(str(kitta_number), 'return')
                        ask_for_more('return')
                        break
                    except ValueError:
                        print("Error: Please enter a valid numeric Kitta Number.")
                        continue

            elif user_choice == 'exit':
                print("Thank you for using TechnoProperty Nepal. Have a Good day!")
                break
            else:
                print("Invalid choice, please choose either 'rent', 'return', or 'exit'.")

        except Exception as e:
            print("An error occurred: ", str(e))


def ask_for_more(action):
    """
    Prompt user whether they want to perform another action on a land.

    Parameters:
        action (str): The action being performed, either 'rent' or 'return'.

    Returns:
        None
    """
    while True:
        more = input("Do you want to " + action + " another land? (yes/no): ").lower()
        if more == 'yes':
            while True:
                try:
                    kitta_number = int(input("Enter the Kitta Number you want to " + action + ": "))
                    operation.interact_land(str(kitta_number), action)
                    break
                except ValueError:
                    print("Error: Please enter a valid numeric Kitta Number.")
                    continue
        elif more == 'no':
            print("Thank you for using TechnoProperty Nepal. Goodbye!")
            break
        else:
            print("Please respond with 'yes' or 'no'.")
            continue


Welcome()
