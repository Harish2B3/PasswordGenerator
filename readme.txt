# Password Generator Project

## Overview:
This is a password generator tool that can generate random passwords based on user-selected criteria or from user details. The application offers two primary functionalities:
1. **Generate Random Password** – Create random passwords with customizable complexity.
2. **Generate Password from User Details** – Generate a password by randomly selecting user-provided details and inserting a special character.

The program is designed to be both user-friendly and secure, offering an interactive menu with color-coded text for easy navigation.

---

## Features:
- **Generate Random Password**:
    - Alphabetic password (letters only).
    - Alphabetic + Numeric password.
    - Alphabetic + Special Character password.
    - Alphabetic + Numeric + Special Character password.

- **Generate Password from User Details**:
    - Prompts the user for personal details (name, surname, date of birth).
    - Randomly selects two details and combines them to form a password.
    - A special character is randomly inserted into the password.

- **Clipboard Support**: Generated passwords are automatically copied to the clipboard for easy use.

- **Color-Coded Interface**: The interface uses colors for better readability and ease of use, utilizing the `colorama` library.

---

## Requirements:
1. Python 3.x
2. Required Python Libraries:
    - `random`
    - `string`
    - `pyperclip`
    - `colorama` (for colored output)

To install the required libraries, run the following commands:

```bash
pip install pyperclip colorama
```

---

## How to Use:
1. **Running the Program**:
    - Open a terminal and navigate to the project directory.
    - Run the program by executing:
    ```bash
    python password_generator.py
    ```

2. **Main Menu**:
    - After running the program, a menu will appear with the following options:
        1. **Generate Random Password**: Choose the type of password you want (alphabetic, alphanumeric, with special characters, etc.).
        2. **Generate Password from User Details**: Input your details (first name, last name, DOB) to generate a password.
        3. **Exit**: Quit the program.

3. **Password Generation Options**:
    - For **Generate Random Password**, you can select from:
        - Alphabetic Password (letters only)
        - Alphabetic + Numeric Password (letters and numbers)
        - Alphabetic + Special Characters Password (letters and symbols)
        - Alphabetic + Numeric + Special Characters Password
    - The program will automatically copy the generated password to the clipboard for convenience.

4. **Security Note**:
    - **Do not use personal information** like names or dates of birth in real passwords, as they are easily hackable. This demo uses personal details to show how passwords can be generated but is not recommended for real use.

---

## Example of Output:

```
========================================
      WELCOME TO PASSWORD GENERATOR
========================================
> 1) Generate Random Password
> 2) Generate Password from User Details
> 3) Exit
========================================
Enter your choice: 1

========================================
PASSWORD OPTIONS
========================================
> 1) Alphabetic Password
> 2) Alphabetic + Numeric Password
> 3) Alphabetic + Special Character Password
> 4) Alphabetic + Numeric + Special Character Password
> 5) Back to Main Menu
========================================
Enter your choice: 4

========================================
Generated Password: J6gS#yVt0qX@jTkL9zWcK
========================================
Password copied to clipboard!

Press Enter to continue...
```

---

## License:
This project is open source and available under the [MIT License](LICENSE).

---

## Credits:
- **Developed by**: [Harish2B3]
- **Libraries Used**:
    - `pyperclip` – For clipboard functionality.
    - `colorama` – For colorful terminal output.

---