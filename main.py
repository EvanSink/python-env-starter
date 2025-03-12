data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Code from my starter chatbot!


def __init__(self, data):
    self.data = data

def chatbot_greet():
    print("Hello, Welcome to Fashion Retail Assistant! I'm here to help you with returns and exchanges.")

def get_user_name():
    return input("Please enter your name: ")

def get_order_number():
    return input("Please enter your order number (8 digits): ")

def validate_order_number(order_number):
    # In a real implementation, this would check against a database
    return len(order_number) == 8 and order_number.isdigit()

def greet_user(name):
    print(f"Thank you, {name}! I'm happy to help you with your return or exchange.")

def help_options():
    print("\nWhat would you like to do?")
    print("1. Return an item")
    print("2. Exchange an item")
    print("3. Check return status")
    print("4. Exit")

def process_return():
    reason = input("Please select the reason for your return:\n"
                  "1. Wrong size\n"
                  "2. Different from picture\n"
                  "3. Quality issues\n"
                  "4. Changed mind\n"
                  "Your choice: ")

    print("\nThank you for providing the reason. Here's what happens next:")
    print("1. You'll receive a return shipping label via email")
    print("2. Pack the item in its original packaging")
    print("3. Attach the shipping label and drop off at any postal location")
    print("4. Refund will be processed within 3-5 business days after we receive the item")

def process_exchange():
    print("\nTo process your exchange:")
    item_type = input("What type of item would you like to exchange? (e.g., shirt, pants, dress): ")
    new_size = input(f"What size would you like to exchange your {item_type} for?: ")
    print(f"\nGreat! We'll process an exchange for your {item_type} in size {new_size}")
    print("1. You'll receive a return shipping label via email")
    print("2. Once we receive your original item, we'll ship your new size")
    print("3. You'll receive tracking information for your new item")

def check_return_status(order_number):
    # In a real implementation, this would check against a database
    print(f"\nChecking status for order {order_number}...")
    print("Your return is in process. Expected refund date: 5 business days")

def help_case():
    while True:
        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            order_number = get_order_number()
            if validate_order_number(order_number):
                process_return()
            else:
                print("Invalid order number. Please try again.")
        elif choice == "2":
            order_number = get_order_number()
            if validate_order_number(order_number):
                process_exchange()
            else:
                print("Invalid order number. Please try again.")
        elif choice == "3":
            order_number = get_order_number()
            if validate_order_number(order_number):
                check_return_status(order_number)
            else:
                print("Invalid order number. Please try again.")
        elif choice == "4":
            print("Thank you for using Fashion Retail Assistant. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

        if choice in ["1", "2", "3"]:
            continue_chat = input("\nIs there anything else I can help you with? (yes/no): ")
            if continue_chat.lower() != "yes":
                print("Thank you for using Fashion Retail Assistant. Have a great day!")
                break

def main():
    chatbot_greet()
    user_name = get_user_name()
    greet_user(user_name)
    help_options()
    help_case()

if __name__ == "__main__":
    main()
