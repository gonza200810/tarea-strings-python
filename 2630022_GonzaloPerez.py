
# COVER PAGE
# Student name: José Gonzalo Reyna Pérez
# Student ID: José Gonzalo Reyna Pérez
# Group: I.M 1-2
# Assignment: Python Collections - Lists, Tuples, and Dictionaries


# EXECUTIVE SUMMARY
# A list is an ordered, mutable collection.
# A tuple is ordered but immutable.
# A dictionary stores key-value pairs.
# Lists are useful for shopping items and grades.
# Tuples are useful for fixed data such as coordinates.
# Dictionaries are useful for catalogs and contact books.
# This program contains six practical problems.
# Each problem includes normal and boundary test cases.

# GOOD PRACTICES
# Use lists for collections that change.
# Use tuples for data that should not change.
# Use dictionaries to search for information by key.
# Use clear variable names and readable code.


# PROBLEM 1: SHOPPING LIST
# Description: Add products and search for an item.
# Inputs: Initial products, new product, search product.
# Outputs: Product list, total items, and search result.
# Validations: Entries must not be empty.
# Normal test: apple, banana; add orange; search apple.
# Boundary test: apple; add apple; search pear.


def problem_1():
    initial_items_text = input(
        "Enter products separated by commas: "
    ).strip()
    new_item = input("Enter a product to add: ").strip()
    search_item = input("Enter a product to search for: ").strip()

    if not initial_items_text or not new_item or not search_item:
        print("Error: invalid input")
        return

    items_list = [
        item.strip()
        for item in initial_items_text.split(",")
        if item.strip()
    ]

    if not items_list:
        print("Error: invalid input")
        return

    items_list.append(new_item)

    is_in_list = search_item.lower() in [
        item.lower() for item in items_list
    ]

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(is_in_list).lower())



# PROBLEM 2: POINTS AND DISTANCES WITH TUPLES
# Description: Calculate distance and midpoint between two points.
# Inputs: x1, y1, x2, y2.
# Outputs: Points, distance, and midpoint.
# Validations: Inputs must be numeric.
# Normal test: (0, 0) and (3, 4) -> distance 5.
# Boundary test: (2, 2) and (2, 2) -> distance 0.


def problem_2():
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        point_a = (x1, y1)
        point_b = (x2, y2)

        distance = (
            (x2 - x1) ** 2 + (y2 - y1) ** 2
        ) ** 0.5

        midpoint = (
            (x1 + x2) / 2,
            (y1 + y2) / 2
        )

        print("Point A:", point_a)
        print("Point B:", point_b)
        print("Distance:", round(distance, 2))
        print("Midpoint:", midpoint)

    except ValueError:
        print("Error: invalid input")



# PROBLEM 3: PRODUCT CATALOG WITH DICTIONARY
# Description: Find product prices and calculate the total.
# Inputs: Product name and quantity.
# Outputs: Unit price, quantity, and total.
# Validations: Product must exist and quantity must be positive.
# Normal test: apple, quantity 3 -> total 30.
# Boundary test: pear, quantity 1 -> total 15.


def problem_3():
    product_prices = {
        "apple": 10.0,
        "banana": 5.0,
        "orange": 8.0,
        "pear": 15.0,
    }

    product_name = input(
        "Enter product name: "
    ).strip().lower()

    try:
        quantity = int(input("Enter quantity: "))

        if not product_name or quantity <= 0:
            print("Error: invalid input")
            return

        if product_name not in product_prices:
            print("Error: product not found")
            return

        unit_price = product_prices[product_name]
        total_price = unit_price * quantity

        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", round(total_price, 2))

    except ValueError:
        print("Error: invalid input")



# PROBLEM 4: STUDENT GRADES WITH LIST AND DICTIONARY
# Description: Calculate a student's average and passing status.
# Inputs: Student name.
# Outputs: Grades, average, and passing status.
# Validations: Student must exist and have grades.
# Normal test: Alice -> average 90, passed.
# Boundary test: Charlie -> average 66.67, not passed.


def problem_4():
    student_grades = {
        "Alice": [90.0, 85.0, 95.0],
        "Bob": [70.0, 75.0, 80.0],
        "Charlie": [60.0, 70.0, 70.0],
    }

    student_name = input(
        "Enter student name: "
    ).strip()

    if not student_name:
        print("Error: invalid input")
        return

    if student_name not in student_grades:
        print("Error: student not found")
        return

    grades_list = student_grades[student_name]

    if not grades_list:
        print("Error: no grades available")
        return

    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0

    print("Grades:", grades_list)
    print("Average:", round(average, 2))
    print("Passed:", str(is_passed).lower())



# PROBLEM 5: WORD FREQUENCY COUNTER
# Description: Count words and find the most frequent word.
# Inputs: A sentence.
# Outputs: Words, frequencies, and most common word.
# Validations: The sentence must not be empty.
# Normal test: "cat dog cat" -> cat appears twice.
# Boundary test: "hello" -> hello appears once.


def problem_5():
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    for punctuation in ".,!?;:":
        sentence = sentence.replace(punctuation, "")

    words_list = sentence.lower().split()

    if not words_list:
        print("Error: invalid input")
        return

    frequency_dict = {}

    for word in words_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    most_common_word = max(
        frequency_dict,
        key=frequency_dict.get
    )

    print("Words list:", words_list)
    print("Frequencies:", frequency_dict)
    print("Most common word:", most_common_word)



# PROBLEM 6: SIMPLE CONTACT BOOK
# Description: Add, search, or delete contacts.
# Inputs: Action, contact name, and phone number if adding.
# Outputs: A message describing the operation.
# Validations: Action and contact information must be valid.
# Normal test: Add Dana with phone 5551234.
# Boundary test: Search for Alice, an existing contact.


def problem_6():
    contacts = {
        "Alice": "1234567890",
        "Bob": "5551234567",
    }

    action_text = input(
        "Enter action (ADD, SEARCH, DELETE): "
    ).strip().upper()

    if action_text not in ("ADD", "SEARCH", "DELETE"):
        print("Error: invalid input")
        return

    name = input("Enter contact name: ").strip()

    if not name:
        print("Error: invalid input")
        return

    if action_text == "ADD":
        phone = input("Enter phone number: ").strip()

        if not phone:
            print("Error: invalid input")
            return

        contacts[name] = phone
        print("Contact saved:", name, contacts[name])

    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")



# MAIN MENU


def main():
    problem_functions = {
        "1": problem_1,
        "2": problem_2,
        "3": problem_3,
        "4": problem_4,
        "5": problem_5,
        "6": problem_6,
    }

    while True:
        print("\nPYTHON COLLECTIONS")
        print("1. Shopping list")
        print("2. Points and distances")
        print("3. Product catalog")
        print("4. Student grades")
        print("5. Word frequency")
        print("6. Contact book")
        print("0. Exit")

        choice = input("Select a problem: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        selected_problem = problem_functions.get(choice)

        if selected_problem is None:
            print("Error: invalid input")
        else:
            selected_problem()


if __name__ == "__main__":
    main()



# CONCLUSIONS
# Lists are useful for collections that change.
# Tuples are useful for fixed data such as coordinates.
# Dictionaries store information using keys and values.
# Lists can store grades and other values.
# Dictionaries can contain lists.
# Validation helps prevent missing or invalid information.

# REFERENCES
# 1. Python Built-in Types:
# https://docs.python.org/3/library/stdtypes.html
# 2. Python Data Structures:
# https://docs.python.org/3/tutorial/datastructures.html
# 3. Python Lists:
# https://docs.python.org/3/tutorial/introduction.html#lists
# 4. Python Dictionaries:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# 5. Python Built-in Functions:
# https://docs.python.org/3/library/functions.html
# 6. Python Errors and Exceptions:
# https://docs.python.org/3/tutorial/errors.html
