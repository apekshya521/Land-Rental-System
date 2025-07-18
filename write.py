from datetime import datetime

def generate_invoice(land_details, customer_name, rent_duration, transaction_type, file_mode='w', fine=None):
    """
    Generate an invoice based on rental details, customer name, rent duration, and transaction type.

    Parameters:
        land_details (tuple): Rental details (kitta_number, city_district, direction, anna, price).
        customer_name (str): Name of the customer.
        rent_duration (int): Duration of rent in months.
        transaction_type (str): Type of transaction ('rent' or 'return').
        file_mode (str, optional): File mode for opening the invoice file. Default is 'w'.
        fine (int, optional): Fine amount for late returns. Default is None.

    Returns:
        None
    """
    # Get current date and time
    current_datetime = datetime.now()
    # Extract rental details
    kitta_number, city_district, direction, anna, price = land_details
    # Calculate total amount
    total_amount = int(price) * int(rent_duration)

    # Prepare invoice content
    invoice_content = ""
    if transaction_type == "rent":
        invoice_content += "Rent Invoice\n\n"
    elif transaction_type == "return":
        invoice_content += "Return Invoice\n\n"

    invoice_content += "Kitta Number: " + str(kitta_number) + "\n"
    invoice_content += "City/District: " + str(city_district) + "\n"
    invoice_content += "Direction: " + str(direction) + "\n"
    invoice_content += "Area (Anna): " + str(anna) + "\n"
    invoice_content += "Price (NPR): " + str(price) + "\n"
    invoice_content += "Customer Name: " + str(customer_name) + "\n"
    invoice_content += "Rent Duration (months): " + str(rent_duration) + "\n"
    invoice_content += "Total Amount (NPR): " + str(total_amount) + "\n\n"

    if fine is not None:
        invoice_content += "Fine for returning late: " + str(fine) + "\n"

    if transaction_type == "rent":
        invoice_content += "Rental Date: " + str(current_datetime) + "\n"
    elif transaction_type == "return":
        invoice_content += "Return Date: " + str(current_datetime) + "\n"

    # Write invoice content to file
    invoice_filename = "Invoice_" + str(customer_name) + "_" + str(transaction_type) + ".txt"
    with open(invoice_filename, file_mode) as invoice_file:
        invoice_file.write(invoice_content)

    # Append total amount to grand total file
    with open("grand_total.txt", "a") as total_file:
        total_file.write(str(total_amount) + "\n")


def return_invoice(customer_name, rent_duration, kitta_number, return_back, land_return, today_date_and_time, file_mode='w', fine=None):
    """
    Generate an invoice for returning a rented property.

    Parameters:
        customer_name (str): Name of the customer.
        rent_duration (int): Duration of rent in months.
        kitta_number (int): Kitta number of the land.
        return_back (datetime): Date and time when the property is returned.
        land_return (tuple): Rental details (kitta_number, city_district, direction, anna, price).
        today_date_and_time (datetime): Current date and time.
        file_mode (str, optional): File mode for opening the invoice file. Default is 'w'.
        fine (int, optional): Fine amount for late returns. Default is None.

    Returns:
        None
    """
    # Extract rental details
    kitta_number, city_district, direction, anna, price = land_return
    # Calculate total amount
    total_amount = int(price) * int(rent_duration)

    # Prepare invoice content
    invoice_content = ""
    invoice_content += "Kitta Number: " + str(kitta_number) + "\n"
    invoice_content += "City/District: " + str(city_district) + "\n"
    invoice_content += "Direction: " + str(direction) + "\n"
    invoice_content += "Area (Anna): " + str(anna) + "\n"
    invoice_content += "Price (NPR): " + str(price) + "\n"
    invoice_content += "Customer Name: " + str(customer_name) + "\n"
    invoice_content += "Rent Duration (months): " + str(rent_duration) + "\n"
    invoice_content += "Total Amount (NPR): " + str(total_amount) + "\n\n"

    if fine is not None:
        invoice_content += "Fine for returning late: " + str(fine) + "\n"

    # Write invoice content to file
    return_filename = "Invoice_" + str(customer_name) + "_Return.txt"
    with open(return_filename, file_mode) as invoice_file:
        invoice_file.write(invoice_content)