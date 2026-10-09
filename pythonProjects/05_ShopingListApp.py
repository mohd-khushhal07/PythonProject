# shoping_List = ["Milk", "Egg", "Bread"]

# # print(shoping_List[1])

# shoping_List.append("Butter")
# shoping_List.insert(1,"Jucie")


# print(shoping_List)
# shoping_List.sort()
# print(shoping_List)

# shoping_List.reverse()

# print(shoping_List)

# shoping_List.clear()
# print(shoping_List)

# # shoping_List.remove("Bread")
# # print(shoping_List)

# # shoping_List.pop(0)
# # print(shoping_List)

# # for item in shoping_List:
# #     print(f" - {item}")

# # for index , item in enumerate(shoping_List):
# #     print(f"{index +1}.{item}")

# Shoping List App

#Step 1: Intialize an empty shopping list

shoppin_list =[]

#Step 2: Define the main menu

def show_menu():
    print("\n---Shoping List Menu---")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. REmove an item")
    print("4. Clear list")
    print("5. Exit")

#Step 3: Main Program loop
while True:
    show_menu() 
    choice = input("ener your choice (1-5): ")

    if choice == "1":
        print("\n---Shoping List---")
        if not shoppin_list:
            print("Your shopping list is empty.")
        else:
            for index, item in enumerate(shoppin_list):
                print(f"{index + 1}. {item}")
    elif choice == "2":
        item = input ("Enter the item to add: ")
        shoppin_list.append(item)
        print(f"{item} has been added to the shopping list. ")
    elif choice == "3":
        item = input ("Enter the item to remove: ")
        shoppin_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    elif choice == "4":
        shoppin_list.clear()
        print("The shopping list has been cleared.")

    elif choice == "5":
        print("Good byee! Happy Shopping")
        break