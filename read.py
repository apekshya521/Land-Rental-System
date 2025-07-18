def Rent_details():
    with open("land.txt", "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]  # Remove the last character, which is '\n'
            if line:
                line_parts = line.split(",")
                if len(line_parts) == 6:
                    kitta_number, city_district, direction, anna, price, availability = line_parts
                    print("\t" + kitta_number + "\t\t" + city_district + "\t\t" + direction + "\t\t" + anna + "\t\t" + price + "\t\t" + availability)
        



