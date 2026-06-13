def control_signal(vehicle_count):
    if vehicle_count > 50:
        green_time = 60
    elif vehicle_count > 20:
        green_time = 40
    else:
        green_time = 20

    print("Vehicle Count:", vehicle_count)
    print("Green Signal Duration:", green_time, "seconds")

while True:
    count = int(input("Enter vehicle count: "))
    control_signal(count)

    choice = input("Continue? (y/n): ")
    if choice.lower() != "y":
        break
