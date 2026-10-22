
# Project: Logic Box
# Pattern Generator and Number Analyzer

print("=" * 45)
print("   PATTERN GENERATOR AND NUMBER ANALYZER")
print("=" * 45)

print("\nWelcome!")
print("This program generates patterns and analyzes numbers.")
print("Please select an option from the menu.")


# Function 1: Pattern Generator
def pattern_generator():
    while True:
        print("\n--- Pattern Generator ---")
        print("1. Right-Angled Triangle")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            rows_input = input("Enter the number of rows: ")

            if not rows_input.isdigit():
                print("Error: Please enter a positive integer.")
                continue

            rows = int(rows_input)

            if rows <= 0:
                print("Error: Rows must be positive.")
                break

            print("\nPattern:")

            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print("*", end="")
                print()

        elif choice == "2":
            break

        else:
            print("Invalid choice. Please try again.")


# Function 2: Number Analyzer
def number_analyzer():
    while True:
        try:
            start = int(input("\nEnter the start of the range: "))
            end = int(input("Enter the end of the range: "))
        except ValueError:
            print("Error: Please enter valid integers.")
            continue

        if end < start:
            print("Error: End must be greater than or equal to start.")
            continue

        total = 0

        print("\nNumber Analysis:")

        for number in range(start, end + 1):
            if number % 2 == 0:
                print(f"Number {number} is Even")
            else:
                print(f"Number {number} is Odd")

            total += number

        print(f"\nSum of all numbers from {start} to {end} is: {total}")
        break


# Main Menu
while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pattern_generator()

    elif choice == "2":
        number_analyzer()

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
