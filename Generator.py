import os
import random
import string
import pyperclip
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def generate_random_password(choice):
    try:
        length = 25

        if choice == 1:
            characters = string.ascii_letters
        elif choice == 2:
            characters = string.ascii_letters + string.digits
        elif choice == 3:
            characters = string.ascii_letters + string.punctuation
        elif choice == 4:
            characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        
        print(f"\n{Fore.GREEN}{'='*40}")
        print(f"{Fore.CYAN}Generated Password: {Fore.YELLOW}{password}")
        print(f"{Fore.GREEN}{'='*40}")
        pyperclip.copy(password)
        print(f"{Fore.GREEN}Password copied to clipboard!\n")
        print('\n')

    except ValueError:
        print(f"{Fore.RED}\nInvalid input. Please enter a number between 1 and 4.")

def generate_password_from_user_details():
    try:
        first_name = input(f"{Fore.MAGENTA}Enter your first name: {Fore.RESET}")
        last_name = input(f"{Fore.MAGENTA}Enter your last name: {Fore.RESET}")
        dob = input(f"{Fore.MAGENTA}Enter your date of birth (DD/MM/YYYY): {Fore.RESET}")
        list_of_details = [first_name, last_name, dob]
        selected_details = random.sample(list_of_details, 2)
        password = ''.join(selected_details)
        password = list(password)
        random_special_char = random.choice(string.punctuation)
        random_pos = random.randint(0, len(password) - 1)
        password[random_pos] = random_special_char

        password = ''.join(password)

        print(f"\n{Fore.GREEN}{'='*40}")
        print(f"{Fore.CYAN}Generated Password: {Fore.YELLOW}{password}")
        print(f"{Fore.GREEN}{'='*40}")
        pyperclip.copy(password)
        print(f"{Fore.GREEN}Password copied to clipboard!\n")
        print(f"{Fore.RED}Note: Never use passwords with personal details (name, DOB). Such passwords are easily hackable.\n")
        print('\n')

    except ValueError:
        print(f"{Fore.RED}\nInvalid input. Please enter valid details.")

def main():
    while True:
        os.system('cls')
        print(f"{Fore.BLUE}{'='*40}")
        print(f"{Fore.YELLOW}{' ' * 12}WELCOME TO PASSWORD GENERATOR")
        print(f"{Fore.BLUE}{'='*40}")
        print(f"{Fore.GREEN}> 1) Generate Random Password")
        print(f"{Fore.GREEN}> 2) Generate Password from User Details")
        print(f"{Fore.GREEN}> 3) Exit")
        print(f"{Fore.BLUE}{'='*40}")

        try:
            ch = int(input(f"{Fore.CYAN}Enter your choice: {Fore.RESET}"))
        except ValueError:
            print(f"{Fore.RED}\nInvalid input. Please enter a number between 1 and 3.")
            input(f"{Fore.CYAN}Press Enter to continue...{Fore.RESET}")
            continue

        if ch == 1:
            print(f"\n{Fore.GREEN}{'='*40}")
            print(f"{Fore.YELLOW}PASSWORD OPTIONS")
            print(f"{Fore.GREEN}{'='*40}")
            print(f"{Fore.GREEN}> 1) Alphabetic Password")
            print(f"{Fore.GREEN}> 2) Alphabetic + Numeric Password")
            print(f"{Fore.GREEN}> 3) Alphabetic + Special Character Password")
            print(f"{Fore.GREEN}> 4) Alphabetic + Numeric + Special Character Password")
            print(f"{Fore.GREEN}> 5) Back to Main Menu")
            print(f"{Fore.GREEN}{'='*40}")

            try:
                choice = int(input(f"{Fore.CYAN}Enter your choice: {Fore.RESET}"))
            except ValueError:
                print(f"{Fore.RED}\nInvalid input. Please enter a number between 1 and 5.")
                input(f"{Fore.CYAN}Press Enter to continue...{Fore.RESET}")
                continue

            if choice == 5:
                continue
            elif choice in [1, 2, 3, 4]:
                generate_random_password(choice)
            else:
                print(f"{Fore.RED}Invalid Choice. Try again.\n")
                input(f"{Fore.CYAN}Press Enter to continue...{Fore.RESET}")

        elif ch == 2:
            generate_password_from_user_details()
        elif ch == 3:
            print(f"{Fore.GREEN}{'='*40}")
            print(f"{Fore.YELLOW}Exiting...")
            print(f"{Fore.GREEN}{'='*40}")
            print(f"{Fore.CYAN}Thank you for using this password generator!.\nTry out our other programs list in github 'https://github.com/Harish2B3/'")
            exit()
        else:
            print(f"{Fore.RED}Invalid Choice. Try again.\n")

        print(f"{Fore.GREEN}{'='*40}")
        print(f"{Fore.CYAN}Press Enter to continue...")
        input()

main()
