# Dictionary to hold room bookings
rooms = {
    101: [], 102: [], 103: [], 104: [], 105: []
}

# Room rates stored as a dictionary
room_rates = {
    "Single": 50.00, "Double": 80.00,
    "Suite": 150.00, "Penthouse": 300.00
}

# Function to get guest name and validate input
def get_guest_name():
    flag = True
    while flag:
        guest_name = input('Enter guest name: ')
        if guest_name.isnumeric():
            print("Invalid name. Try again.")
            flag = True
        else:
            guest_name = "Guest: {}".format(guest_name.capitalize())
            flag = False
    return guest_name

# Function to get room number and validate input
def get_room_num():
    flag = True
    while flag:
        room_num = input('Enter room number: ')
        try:
            room_num = int(room_num)
            if room_num not in rooms:
                print("Room number must be between 101 and 105")
                flag = True
            else:
                flag = False
        except ValueError:
            print("Invalid room number. Try again.")
    return room_num

# Function to get room type and validate input
def get_room_type():
    flag = True
    while flag:
        room_type = input('Enter room type (Single, Double, Suite, Penthouse): ')
        if room_type.lower().capitalize() not in room_rates:
            print("Invalid room type. Try again.")
            flag = True
        else:
            room_type = room_type.capitalize()
            flag = False
    return room_type

# Function to get number of nights and validate input
def get_nights():
    flag = True
    while flag:
        nights = input('Enter number of nights: ')
        try:
            nights = int(nights)
            if nights < 1:
                print("Nights must be at least 1.")
                flag = True
            else:
                flag = False
        except ValueError:
            print("Invalid input. Must be a number.")
    return nights

enter_booking = True

while enter_booking:
    print("###############################################")
    print("#### Welcome to the Hotel Booking System ####")
    print("###############################################")
    print("")
    print("1. Enter new booking")
    print("2. View bill")
    print("3. Exit")
    print("")

    temp = True
    while temp:
        choice = input('Enter option: ')
        try:
            choice = int(choice)
            temp = False
        except ValueError:
            print("Not an option.")


    if choice == 1:
        guest_name = get_guest_name()
        room_num = get_room_num()
        room_type = get_room_type()
        nights = get_nights()
        cost = room_rates[room_type] * nights
        rooms[room_num] = [guest_name, room_type, nights, cost]

    elif choice == 2:
        room_num = get_room_num()
        test = False
        try:
            rooms[room_num][0]
            test = False
        except IndexError:
            test = True
        if rooms[room_num] == "" or test:
            print("No booking found for this room.")
        else:
            print(str(rooms[room_num][0]))
            print("Room type: " + str(rooms[room_num][2]))
            print("Number of nights: " + str(rooms[room_num][1]))
            print("Total cost: " + str(rooms[room_num][3]))

    elif choice == 3:
        break

    else:
        print("Invalid option. Try again.")
