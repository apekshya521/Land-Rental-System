from datetime import datetime

today_date_and_time = datetime.now()
rent_totals = {}
return_totals = {}


def interact_land(kitta_number, action):
    """
    Interact with land records based on the provided action.

    Parameters:
        kitta_number (str): The Kitta number of the land.
        action (str): The action to perform, either 'rent' or 'return'.

    Returns:
        None
    """
    var = "qwertyuiopasdfghjklzxcvbnm"
    found = False
    successful = False
    lines = []

    with open("land.txt", "r+") as file:  # Open file in read and write mode
        lines = file.readlines()

        for i, line in enumerate(lines):
            line_parts = line.split(",")
            if line_parts[0] == kitta_number:
                found = True
                availability = line_parts[5].replace("\n", "")
                if action == "rent" and availability.lower() == 'available':
                    anna_to_rent = int(input("Enter the number of anna you want to rent : "))
                    if anna_to_rent == int(line_parts[3]):
                        while True:
                            customer_name = input("Enter your name: ")
                            invalid_name = False
                            for char in customer_name:
                                if char not in var:
                                    invalid_name = True
                                    break
                            if invalid_name:
                                print("Invalid name! Please enter a name without special characters or digits.")
                            else:
                                break
                        rent_duration = int(input("Enter the duration of rent (in months): "))  # Corrected to integer

                        # Update availability status to 'Not Available'
                        lines[i] = line.replace("Available", "Not Available")
                        successful = True
                        # Generate rental invoice
                        generate_invoice(line_parts, customer_name, rent_duration, action, file_mode='a')
                    else:
                        print("Error: You must rent the available (", line_parts[3], "anna).")
                elif action == "return" and availability.lower() == 'not available':
                    anna_to_return = int(input("Enter the number of anna you are returning: "))
                    if anna_to_return == int(line_parts[3]):
                        while True:
                            customer_name = input("Enter your name: ")
                            invalid_name = False
                            for char in customer_name:
                                if char not in var:
                                    invalid_name = True
                                    break
                            if invalid_name:
                                print("Invalid name! Please enter a name without special characters or digits.")
                            else:
                                break
                        rent_duration = int(input("Enter the original rent duration  (in months): "))  # Corrected to integer

                        lines[i] = line.replace("Not Available", "Available")
                        successful = True

                        return_back = int(input("Enter the return back duration (in months): "))

                            # Calculate late return fine
                        if rent_duration < return_back:
                            late_months = return_back - rent_duration
                            fine = late_months * int(line_parts[4]) * 0.10
                            print("Fine for returning late:", fine)
                            print("Land is successfully returned by ", customer_name)
                                # Generate return invoice
                            return_invoice(customer_name, rent_duration, kitta_number, anna_to_return, line_parts,
                                               return_back, fine, file_mode='a')
                        else:
                                # Generate return invoice without fine
                            return_invoice(customer_name, rent_duration, kitta_number, anna_to_return, line_parts,
                                               return_back, file_mode='a')
                    else:
                        print("Error: You must return the same (", line_parts[3], "anna you purchased).")

        # Write back modified lines to the file
        file.seek(0)
        file.writelines(lines)

    if found and not successful:
        action_desc = 'not available for rent' if action == 'rent' else 'already available for return'
        print("failed: Land is", action_desc)
    elif not found:
        print("Land with Kitta Number", kitta_number, "is not found.")

    if action == "rent":
        print("Rent Grand Total up to here: ", end="")
        for total in rent_totals.values():
            print(str(total) + ", ", end="")
        print("\b\b")
    elif action == "return":
        print("Return Grand Total up to here: ", end="")
        for total in return_totals.values():
            print(str(total) + ", ", end="")
        print("\b\b")


def generate_invoice(land_details, customer_name, rent_duration, action, file_mode='w'):
    """
    Generate an invoice for rental or return.

    Parameters:
        land_details (list): Details of the land.
        customer_name (str): The name of the customer.
        rent_duration (int): The duration of the rent in months.
        action (str): The action for which the invoice is generated, either 'rent' or 'return'.
        file_mode (str): The file mode for opening the invoice file.

    Returns:
        None
    """
    kitta_number = land_details[0]
    city_district = land_details[1]
    direction = land_details[2]
    anna = land_details[3]
    price = land_details[4]
    rental_date = str(today_date_and_time.year) + "-" + str(today_date_and_time.month).zfill(2) + "-" + str(
        today_date_and_time.day).zfill(2)

    total_amount = int(price) * rent_duration  # Corrected to multiply with integer rent_duration

    print("Invoice Details:")
    print("************************")
    print("Kitta Number: ", kitta_number)
    print("City/District: ", city_district)
    print("Direction: ", direction)
    print("Area (Anna): ", anna)
    print("Price (NPR): ", price)
    print("Customer Name: ", customer_name)
    print("Rent Duration (months): ", rent_duration)
    print("Rental Date: ", rental_date)
    print("Total Amount (NPR): ", total_amount)
    #print("Grand Total up to here:", ', '.join(map(str, customer_totals.values())))

    #print("Rental Date: ", rental_date)
    print("----------------------------")

    # Update rent totals
    if customer_name in rent_totals:
        rent_totals[customer_name] += total_amount
    else:
        rent_totals[customer_name] = total_amount

    invoice_filename = "Invoice_" + customer_name + "_" + action + ".txt"
    with open(invoice_filename, file_mode) as invoice_file:  # Use file_mode parameter here
        invoice_file.write("************ " + action.capitalize() + " Invoice ************\n\n")
        invoice_file.write("Kitta Number: " + kitta_number + "\n")
        invoice_file.write("City/District: " + city_district + "\n")
        invoice_file.write("Direction: " + direction + "\n")
        invoice_file.write("Area (Anna): " + anna + "\n")
        invoice_file.write("Price (NPR): " + price + "\n")
        invoice_file.write("Customer Name: " + customer_name + "\n")
        invoice_file.write("Rent Duration (months): " + str(rent_duration) + "\n")
        invoice_file.write("Total Amount (NPR): " + str(total_amount) + "\n")
        invoice_file.write("\nRental Date: " + rental_date + "\n")
        invoice_file.write("\nGrand Total upto here: " + str(rent_totals[customer_name]) + "\n")


def return_invoice(customer_name, rent_duration, kitta_number, anna_returned, land_details, return_back, fine=None,
                   file_mode='w'):
    """
    Generate an invoice for returning rented land.

    Parameters:
        customer_name (str): The name of the customer.
        rent_duration (int): The duration of the rent in months.
        kitta_number (str): The Kitta number of the land.
        anna_returned (int): The number of anna returned.
        land_details (list): Details of the land.
        return_back (int): The return back duration in months.
        fine (float): The fine amount, if any.
        file_mode (str): The file mode for opening the invoice file.

    Returns:
        None
    """
    city_district = land_details[1]
    direction = land_details[2]
    anna = land_details[3]
    price = land_details[4]
    return_date = str(today_date_and_time.year) + "-" + str(today_date_and_time.month).zfill(2) + "-" + str(
        today_date_and_time.day).zfill(2)

    print(" Return Invoice Details:")
    print("****************************")
    print("land of Kitta Number: ", kitta_number)
    print("City/District: ", city_district)
    print("Direction: ", direction)
    print("Area (Anna): ", anna)
    print("Price (NPR): ", price)
    print("Customer Name: ", customer_name)
    print("Rent Duration (months): ", rent_duration, "month")
    print("Return Date  : ", return_date)
    total_amount = int(land_details[4]) * rent_duration
    if rent_duration < return_back:
        left_month = return_back - rent_duration
        fine = left_month * int(land_details[4]) * 0.1
        print("Fine for returning late: ", fine)
        total_amount += fine  # Add fine to the total amount
    print("Total Amount (NPR): ", total_amount)

    '''if rent_duration < return_back:
        left_month = return_back - rent_duration
        fine = left_month * int(land_details[4]) * 0.1
        print("Fine for returning late: ", fine)
        total_amount += fine  # Add fine to the total amount'''
    #print("Grand Total upto here: ", customer_totals[customer_name])
    print("--------------------------------------------")
    print("*")

    # Update return totals
    if customer_name in return_totals:
        return_totals[customer_name] += total_amount
    else:
        return_totals[customer_name] = total_amount

    return_filename = "Invoice_" + customer_name + "_Return.txt"
    with open(return_filename, file_mode) as invoice_file:
        invoice_file.write("************ Return Invoice ************\n\n")
        invoice_file.write("Kitta Number: " + kitta_number + "\n")
        invoice_file.write("City/District: " + city_district + "\n")
        invoice_file.write("Direction: " + direction + "\n")
        invoice_file.write("Area (Anna): " + anna + "\n")
        invoice_file.write("Price (NPR): " + price + "\n")
        invoice_file.write("Customer Name: " + customer_name + "\n")
        invoice_file.write("Rent Duration (months): " + str(rent_duration) + "\n")
        invoice_file.write("\nReturn Date: " + return_date + "\n")
        if fine is not None:
            invoice_file.write("Fine for returning late: " + str(fine) + "\n")
        invoice_file.write("Total Amount (NPR): " + str(total_amount) + "\n")
        #invoice_file.write("\nReturn Date: " + return_date + "\n")
        invoice_file.write("\nGrand Total upto here: " + str(return_totals[customer_name]) + "\n")
