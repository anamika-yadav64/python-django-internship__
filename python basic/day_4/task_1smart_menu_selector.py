def food_menu(choice):
    match choice.lower():
        case "pizza":
            print("Price: ₹250")
        case "burger":
            print("Price: ₹150")
        case "coffee":
            print("Price: ₹100")
        case _:
            print("Item not available")# Example usage
food_menu("pizza")
food_menu("burger")
food_menu("coffee")
food_menu("sandwich")
