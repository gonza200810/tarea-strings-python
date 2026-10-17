# COVER PAGE
# Name:José Gonzalo Reyna Pérez
# Student ID: 2630022
# Group: I.M 1-2
# Assignment: String Processing in Python



# EXECUTIVE SUMMARY
# A string is a sequence of characters in Python.
# Strings are immutable, which means they cannot be changed directly.
# Python strings support concatenation, searching, and text replacement.
# Input validation helps prevent incorrect or empty data.
# Text normalization makes data more consistent.
# This assignment contains six string-processing problems.
# Each problem includes inputs, outputs, validations, and test cases.
# The programs demonstrate practical uses of Python string methods.


# PRINCIPLES AND BEST PRACTICES
# Strings are immutable; string operations create new strings.
# Use lowercase letters and underscores for variable names.
# Validate user input before processing it.
# Avoid repeating code whenever possible.
# Use clear names and meaningful messages.



# PROBLEM 1: FULL NAME FORMATTER
# Description: Format the first name and last name correctly.
# Inputs: First name and last name entered by the user.
# Outputs: The full name with correct capitalization.
# Validations: Neither name can be empty.
# Test case 1 (Normal): "gonzalo", "perez" -> "Gonzalo Perez"
# Test case 2 (Border): "A", "B" -> "A B"


def format_full_name():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    if not first_name or not last_name:
        print("Both names are required.")
        return

    full_name = first_name.title() + " " + last_name.title()
    print("Full name:", full_name)



# PROBLEM 2: SIMPLE EMAIL VALIDATOR
# Description: Check whether an email has a basic valid format.
# Inputs: An email address entered by the user.
# Outputs: A message indicating whether it is valid.
# Validations: Check for @, a local part, and a domain with a dot.
# Test case 1 (Normal): "gonzalo@gmail.com" -> Valid
# Test case 2 (Border): "a@b.co" -> Valid


def validate_email():
    email = input("Enter your email address: ").strip()

    if " " in email or email.count("@") != 1:
        print("Email is invalid.")
        return

    local_part, domain = email.split("@")

    if (
        not local_part
        or not domain
        or "." not in domain
        or domain.startswith(".")
        or domain.endswith(".")
    ):
        print("Email is invalid.")
    else:
        print("Email is valid.")



# PROBLEM 3: PALINDROME CHECKER
# Description: Check whether text reads the same backward.
# Inputs: A word or phrase entered by the user.
# Outputs: A message indicating whether it is a palindrome.
# Validations: The text must not be empty.
# Test case 1 (Normal): "Anita lava la tina" -> Palindrome
# Test case 2 (Border): "A" -> Palindrome

def check_palindrome():
    text = input("Enter a word or phrase: ").strip()

    if not text:
        print("Please enter some text.")
        return

    normalized_text = text.replace(" ", "").lower()
    reversed_text = normalized_text[::-1]

    if normalized_text == reversed_text:
        print("The text is a palindrome.")
    else:
        print("The text is not a palindrome.")



# PROBLEM 4: SENTENCE WORD STATISTICS
# Description: Count the words and characters in a sentence.
# Inputs: A sentence entered by the user.
# Outputs: The number of words and characters.
# Validations: The sentence must not be empty.
# Test case 1 (Normal): "Python is fun" -> 3 words
# Test case 2 (Border): "Hi" -> 1 word, 2 characters


def sentence_statistics():
    sentence = input("Enter a sentence: ")

    if not sentence.strip():
        print("Please enter a sentence.")
        return

    words = sentence.split()
    word_count = len(words)
    character_count = len(sentence)

    print("Word count:", word_count)
    print("Character count:", character_count)



# PROBLEM 5: PASSWORD STRENGTH
# Description: Evaluate the strength of a password.
# Inputs: A password entered by the user.
# Outputs: Weak, medium, or strong.
# Validations: Check length, uppercase, lowercase, digits,
# and special characters.
# Test case 1 (Normal): "SecurePass123!" -> Strong
# Test case 2 (Border): "Aa1!aaaa" -> Strong (8 characters)


def check_password_strength():
    password = input("Enter a password: ")

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    criteria_count = sum([
        has_uppercase,
        has_lowercase,
        has_digit,
        has_special
    ])

    if len(password) < 8:
        strength = "Weak"
    elif criteria_count == 4:
        strength = "Strong"
    elif criteria_count >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    print("Password strength:", strength)



# PROBLEM 6: PRODUCT LABEL
# Description: Format a product label to exactly 30 characters.
# Inputs: A product name or label.
# Outputs: A label of exactly 30 characters.
# Validations: Empty labels are not accepted.
# Short labels are padded with spaces; long labels are truncated.
# Test case 1 (Normal): "Industrial Motor" -> 30 characters
# Test case 2 (Border): A 30-character label -> Unchanged


def format_product_label():
    product_name = input("Enter the product name: ").strip()

    if not product_name:
        print("A product name is required.")
        return

    LABEL_LENGTH = 30
    formatted_label = product_name[:LABEL_LENGTH].ljust(LABEL_LENGTH)

    print("Product label: |" + formatted_label + "|")
    print("Label length:", len(formatted_label))



# MAIN MENU
# Allows the user to choose which problem to run.


def main():
    while True:
        print("\nSTRING PROCESSING PROGRAMS")
        print("1. Full Name Formatter")
        print("2. Simple Email Validator")
        print("3. Palindrome Checker")
        print("4. Sentence Word Statistics")
        print("5. Password Strength")
        print("6. Product Label")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            format_full_name()
        elif choice == "2":
            validate_email()
        elif choice == "3":
            check_palindrome()
        elif choice == "4":
            sentence_statistics()
        elif choice == "5":
            check_password_strength()
        elif choice == "6":
            format_product_label()
        elif choice == "0":
            print("Program finished.")
            break
        else:
            print("Invalid option. Choose a number from 0 to 6.")


if __name__ == "__main__":
    main()



# CONCLUSIONS
# Python strings are useful for processing text information.
# String methods help organize and transform text.
# Input validation helps programs handle incorrect information.
# Functions organize code into reusable sections.
# Testing helps verify that programs produce expected results.
# These techniques are useful in practical programming tasks.



# REFERENCES
# [1] Python Software Foundation, "Text Sequence Type: str."
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# [2] Python Software Foundation, "String Methods."
# https://docs.python.org/3/library/stdtypes.html#string-methods
#
# [3] Python Software Foundation, "Built-in Functions."
# https://docs.python.org/3/library/functions.html
#
# [4] Python Software Foundation, "The Python Tutorial:
# Input and Output."
# https://docs.python.org/3/tutorial/inputoutput.html
#
# [5] Python Software Foundation, "Regular Expression Operations."
# https://docs.python.org/3/library/re.html
