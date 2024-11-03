def get_grades():
    grades = []
    while True:
        try:
            grade = input("Enter a grade (or type 'done' to finish): ")
            if grade.lower() == 'done':
                break
            grade = float(grade)  
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def save_grades_to_file(grades, filename='grades.txt'):
    try:
        with open(filename, 'w') as file:
            for grade in grades:
                file.write(f"{grade}\n")
        print(f"Grades saved to {filename}.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def read_grades_from_file(filename='grades.txt'):
    try:
        with open(filename, 'r') as file:
            grades = [float(line.strip()) for line in file]
        return grades
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
        return []
    except ValueError:
        print("Invalid data found in the file. Ensure all grades are numeric.")
        return []

def main():
    grades = read_grades_from_file()

    print("Current grades:", grades)
    new_grades = get_grades()
    
    if new_grades:
        grades.extend(new_grades)
        average = calculate_average(grades)
        print(f"Average grade: {average:.2f}")
        save_grades_to_file(grades)
    else:
        print("No new grades were added.")

if __name__ == "__main__":
    main()
