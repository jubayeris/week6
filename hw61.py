def convert_and_print_uppercase(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                uppercase_line = line.upper()
                print(uppercase_line, end='')

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter a file name: ")
    convert_and_print_uppercase(filename)
