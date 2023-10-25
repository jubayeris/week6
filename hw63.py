def extract_numbers(line):
    return [float(word) for word in line.split() if word.replace('.', '', 1).isdigit()]

try:
    file_name = input("Enter the name of the file: ")
    total_sum, total_count = 0, 0
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                numbers = extract_numbers(line)
                total_sum += sum(numbers)
                total_count += len(numbers)
    if total_count > 0:
        average = total_sum / total_count
        print(f"Sum of numbers: {total_sum}")
        print(f"Average value: {average:.15f}")
    else:
        print("No valid numbers found in the file.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
