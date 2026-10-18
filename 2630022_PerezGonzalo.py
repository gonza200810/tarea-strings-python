# COVER PAGE
# Student name: José Gonzalo Reyna Pérez
# Student ID: 2630022
# Group: I.M 1-2
# Assignment: Numeric Types and Boolean Values


# EXECUTIVE SUMMARY
# int represents whole numbers, while float represents decimal numbers.
# bool stores one of two values: True or False.
# Comparisons such as >=, ==, and < produce Boolean values.
# Logical operators and, or, and not combine conditions.
# Input validation helps prevent incorrect calculations.
# Range checks prevent impossible values and division by zero.
# This program includes six exercises using numbers and Booleans.
# Each problem includes inputs, outputs, validations, and two test cases.

# GOOD PRACTICES
# Use int for whole numbers and float for decimal quantities.
# Store intermediate results in descriptive variables.
# Validate data before performing calculations.
# Use descriptive variable names and clear output messages.
# True means a condition is met; False means it is not.


# PROBLEM 1: TEMPERATURE CONVERTER
# Description:
# Convert Celsius to Fahrenheit and Kelvin.
# Determine whether the temperature is at least 30 degrees Celsius.

# Inputs: temp_c (float).
# Outputs: Fahrenheit, Kelvin, High temperature.
# Validations: Numeric input and Kelvin >= 0.
# Test cases:
# Normal: 25.0 -> 77.0 F, 298.15 K, False.
# Border: -273.15 -> -459.67 F, 0.0 K, False.

def problem_1():
    try:
        temp_c = float(input("Enter temperature in Celsius: "))
        temp_k = temp_c + 273.15

        if temp_k < 0.0:
            print("Error: invalid input")
            return

        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())

    except ValueError:
        print("Error: invalid input")



# PROBLEM 2: WORK HOURS AND OVERTIME
# Description:
# Calculate weekly pay, including overtime paid at 150%.
# Overtime applies to hours worked above 40.
#
# Inputs: hours_worked (float), hourly_rate (float).
# Outputs: Regular pay, Overtime pay, Total pay, Has overtime.
# Validations: hours_worked >= 0 and hourly_rate > 0.
# Test cases:
# Normal: 45 hours, rate 20 -> regular 800, overtime 150, total 950.
# Border: 40 hours, rate 20 -> regular 800, overtime 0, total 800.

def problem_2():
    try:
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))

        if hours_worked < 0 or hourly_rate <= 0:
            print("Error: invalid input")
            return

        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40.0

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", str(has_overtime).lower())

    except ValueError:
        print("Error: invalid input")



# PROBLEM 3: DISCOUNT ELIGIBILITY
# Description:
# A customer receives a 10% discount if they are a student,
# a senior, or their purchase is at least 1000.
#
# Inputs: purchase_total, is_student_text, is_senior_text.
# Outputs: Discount eligible and Final total.
# Validations: Purchase >= 0; answers must be YES or NO.
# Test cases:
# Normal: 500, YES, NO -> eligible True, total 450.
# Border: 1000, NO, NO -> eligible True, total 900.


def problem_3():
    try:
        purchase_total = float(input("Enter purchase total: "))
        is_student_text = input(
            "Is the customer a student? (YES/NO): "
        ).strip().upper()
        is_senior_text = input(
            "Is the customer a senior? (YES/NO): "
        ).strip().upper()

        if (
            purchase_total < 0
            or is_student_text not in ("YES", "NO")
            or is_senior_text not in ("YES", "NO")
        ):
            print("Error: invalid input")
            return

        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = (
            is_student or is_senior or purchase_total >= 1000.0
        )

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", round(final_total, 2))

    except ValueError:
        print("Error: invalid input")



# PROBLEM 4: BASIC STATISTICS
# Description:
# Calculate the sum, average, maximum, minimum, and determine
# whether all three integers are even.
#
# Inputs: n1, n2, n3 (integers).
# Outputs: Sum, Average, Max, Min, All even.
# Validations: All inputs must be integers.
# Test cases:
# Normal: 2, 4, 6 -> sum 12, average 4, max 6, min 2, True.
# Border: -2, 0, 3 -> sum 1, average 0.33, max 3, min -2, False.


def problem_4():
    try:
        n1 = int(input("Enter the first integer: "))
        n2 = int(input("Enter the second integer: "))
        n3 = int(input("Enter the third integer: "))

        sum_value = n1 + n2 + n3
        average_value = sum_value / 3
        max_value = max(n1, n2, n3)
        min_value = min(n1, n2, n3)

        all_even = (
            n1 % 2 == 0
            and n2 % 2 == 0
            and n3 % 2 == 0
        )

        print("Sum:", sum_value)
        print("Average:", round(average_value, 2))
        print("Max:", max_value)
        print("Min:", min_value)
        print("All even:", str(all_even).lower())

    except ValueError:
        print("Error: invalid input")



# PROBLEM 5: LOAN ELIGIBILITY
# Description:
# Evaluate loan eligibility using income, debt ratio, and credit score.
# Requirements: income >= 8000, ratio <= 0.4, score >= 650.
#
# Inputs: monthly_income, monthly_debt, credit_score.
# Outputs: Debt ratio and Eligible.
# Validations: income > 0, debt >= 0, score >= 0.
# Test cases:
# Normal: income 10000, debt 3000, score 700 -> ratio 0.3, True.
# Border: income 8000, debt 3200, score 650 -> ratio 0.4, True.


def problem_5():
    try:
        monthly_income = float(input("Enter monthly income: "))
        monthly_debt = float(input("Enter monthly debt: "))
        credit_score = int(input("Enter credit score: "))

        if (
            monthly_income <= 0
            or monthly_debt < 0
            or credit_score < 0
        ):
            print("Error: invalid input")
            return

        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print("Debt ratio:", round(debt_ratio, 2))
        print("Eligible:", str(eligible).lower())

    except ValueError:
        print("Error: invalid input")



# PROBLEM 6: BODY MASS INDEX (BMI)
# Description:
# Calculate BMI and classify it as underweight, normal, or overweight.
#
# Inputs: weight_kg (float), height_m (float).
# Outputs: BMI, Underweight, Normal, Overweight.
# Validations: weight_kg > 0 and height_m > 0.
# Test cases:
# Normal: 70 kg, 1.75 m -> BMI 22.86, Normal True.
# Border: 47.36 kg, 1.60 m -> BMI 18.50, Normal True.


def problem_6():
    try:
        weight_kg = float(input("Enter weight in kilograms: "))
        height_m = float(input("Enter height in meters: "))

        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
            return

        bmi = weight_kg / (height_m * height_m)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())

    except ValueError:
        print("Error: invalid input")



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
        print("\nNUMERIC TYPES AND BOOLEAN VALUES")
        print("1. Temperature converter")
        print("2. Work hours and overtime")
        print("3. Discount eligibility")
        print("4. Basic statistics")
        print("5. Loan eligibility")
        print("6. Body mass index")
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
# Integers represent whole numbers, while floats represent decimals.
# Comparisons produce Booleans that help programs make decisions.
# Input validation prevents incorrect values from being processed.
# Checking denominators helps avoid division by zero.
# The and, or, and not operators combine logical conditions.
# These techniques are useful for payroll, discounts, and loans.
# Testing normal and boundary cases helps verify program behavior.


# REFERENCES
# 1. Python Documentation - Built-in Types:
#    https://docs.python.org/3/library/stdtypes.html
# 2. Python Documentation - Numeric Types:
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 3. Python Documentation - Boolean Type:
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 4. Python Documentation - Built-in Functions:
#    https://docs.python.org/3/library/functions.html
# 5. Python Tutorial - Control Flow:
#    https://docs.python.org/3/tutorial/controlflow.html
# 6. Python Tutorial - Errors and Exceptions:
#    https://docs.python.org/3/tutorial/errors.html
