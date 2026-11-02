medicines = [
    {"title": "Aspirin", "price": 50000, "count": 20},
    {"title": "Vitamin C", "price": 80000, "count": 15},
    {"title": "Ibuprofen", "price": 60000, "count": 10}
]
print(medicines)

while True:
    print("1 -> Add Medicine")
    print("2 -> Delete Medicine")
    print("3 -> Show Medicines")
    print("4 -> Find Medicine")
    print("5 -> Sell Medicine")
    print("6 -> Restock Medicine")
    print("7 -> Calculate Inventory Value")
    print("8 -> Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        found = False
        medicine_title = input("Enter Medicine: ")
        for medicine in medicines:
            if medicine["title"] == medicine_title:
                found = True
                new_count = int(input("Enter new count: "))
                medicine["count"] += new_count
                print("Successfully updated medicine")
                break
        if not found:
            new_medicine_price = int(input("Enter new medicine price: "))
            new_medicine_count = int(input("Enter new medicine count: "))
            new_medicine = {"title": medicine_title, "price": new_medicine_price , "count": new_medicine_count}
            medicines.append(new_medicine)
            print("Successfully added medicine")
        print(medicines)

    elif choice == 2:
        medicine_title = input("Enter Medicine: ")
        found = False
        for medicine in medicines:
            if medicine["title"] == medicine_title:
                found = True
                medicines.remove(medicine)
                print("Successfully deleted medicine")
                break
        if not found:
            print("Medicine not found")
    elif choice == 3:
        for medicine in medicines:
            print(f"{medicine['title']} -> {medicine['price']} -> {medicine['count']}")

    elif choice == 4:
        medicine_title = input("Enter Medicine: ")
        found = False
        for medicine in medicines:
            if medicine["title"] == medicine_title:
                found = True
                print(f"title: {medicine['title']}")
                print(f"price: {medicine['price']}")
                print(f"count: {medicine['count']}")


                break
        if not found:
            print("Medicine not found")

    elif choice == 5:
        medicine_title = input("Enter Medicine: ")
        found = False
        for medicine in medicines:
            if medicine["title"] == medicine_title:
                found = True
                sell_count = int(input("Enter new count: "))
                if sell_count <= 0:
                    print("Invalid count")
                elif sell_count <= medicine["count"] :
                    medicine["count"] -= sell_count
                    print("Successfully updated medicine")
                    print(medicines)
                else:
                    print("Insufficient")
                break
        if not found:
            print("Medicine not found")

    elif choice == 6:
        medicine_title = input("Enter Medicine: ")
        found = False
        for medicine in medicines:
            if medicine["title"] == medicine_title:
                found = True
                new_medicine_count = int(input("Enter new count: "))
                medicine["count"] += new_medicine_count
                print("Successfully updated medicine")
                print(medicines)
        if not found:
            print("Medicine not found")

    elif choice == 7:
        total_value = 0
        for medicine in medicines:
            total_value += medicine["price"] * medicine["count"]

        print(f"total_value: {total_value}")

    elif choice == 8:
        print("Exit")
        break
    else:
        print("Invalid choice")




