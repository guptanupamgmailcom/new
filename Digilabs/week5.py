# Import necessary libraries
import getpass
import random

# Define login credentials
credentials = {
    'user1': {'password': 'password1', 'access_fruit_price': False, 'can_change_stock': True},
    'user2': {'password': 'password1', 'access_fruit_price': False, 'can_change_stock': False},
    'user3': {'password': 'password2', 'access_fruit_price': True, 'can_change_stock': False},
    'user4': {'password': 'password2', 'access_fruit_price': False, 'can_change_stock': False},
    'user5': {'password': 'password3', 'access_fruit_price': True, 'can_change_stock': True}
}

# Define fruit stock and price information
fruit_stock = {'apple': 100, 'banana': 200, 'orange': 150}
fruit_price = {'apple': 0.5, 'banana': 0.2, 'orange': 0.3}

# Define function to check login credentials
def check_credentials():
    """
    Function to check if login credentials are valid
    """
    input_username = input('Enter your username: ')
    input_password = getpass.getpass('Enter your password: ')

    if input_username in credentials and input_password == credentials[input_username]['password']:
        # CAPTCHA authentication
        captcha = generate_captcha()
        print('Enter the following CAPTCHA to continue: ' + captcha)
        for i in range(3):
            input_captcha = input('Enter the CAPTCHA: ')
            if input_captcha == captcha:
                return True, credentials[input_username]['access_fruit_price'], credentials[input_username]['can_change_stock'], input_username
            else:
                print('Incorrect CAPTCHA. Please try again.')
        return False, False, False, None
    else:
        return False, False, False, None

# Define function to generate CAPTCHA
def generate_captcha():
    """
    Function to generate a 4-digit CAPTCHA
    """
    captcha = ''
    for i in range(4):
        captcha += str(random.randint(0, 9))
    return captcha

# Main program loop
while True:
    # Check login credentials
    valid_credentials, access_fruit_price, can_change_stock, username = check_credentials()
    if not valid_credentials:
        print('Invalid username or password. Please try again.\n')
        continue

    # Login successful
    print('Login successful.\n')

    # Main menu loop
    while True:
        # Show main menu
        print('\nMain menu:')
        print('a) Change fruit stock')
        print('b) Change password')
        print('c) Log out')

        # Get user input
        user_input = input('\nEnter your choice: ')

        # Option to change fruit stock
        if user_input.lower() == 'a':
            if can_change_stock:
                print('\nFruit stock:')
                for fruit, stock in fruit_stock.items():
                    print(fruit + ': ' + str(stock))
                fruit_to_change = input('\nEnter the name of the fruit you want to change: ')
                if fruit_to_change in fruit_stock:
                    new_stock = input('Enter the new stock value for ' + fruit_to_change + ': ')
                    try:
                        fruit_stock[fruit_to_change] = int(new_stock)
                        print('Fruit stock updated.')
                    except ValueError:
                        print('Invalid stock value. Stock value must be an integer.')
            else:
                print('You do not have the privilege to change fruit stock.')

        # Option to change password
        elif user_input.lower() == 'b':
            if username == 'user3':
                password_to_change = input('\nWhich password do you want to change? (user1)')
