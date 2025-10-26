class StudentsDataException(Exception):
    """Base class for all student data-related exceptions."""
    pass


class BadLine(StudentsDataException):
    """Raised when a line in the file is malformed."""
    pass


class FileEmpty(StudentsDataException):
    """Raised when the file exists but is empty."""
    pass


def read_student_data(filename):
    students = {}

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            if not lines:
                raise FileEmpty("The file exists but is empty.")

            for line_no, line in enumerate(lines, start=1):
                line = line.strip()
                if not line:
                    continue  # skip blank lines

                parts = line.split()
                if len(parts) != 3:
                    raise BadLine(f"Bad line format at line {line_no}: {line}")

                first_name, last_name, points_str = parts

                try:
                    points = float(points_str)
                except ValueError:
                    raise BadLine(f"Invalid points value at line {line_no}: {points_str}")

                key = (first_name, last_name)
                students[key] = students.get(key, 0.0) + points

    except FileNotFoundError:
        raise StudentsDataException(f"File '{filename}' not found.")
    except IOError:
        raise StudentsDataException(f"Error reading file '{filename}'.")

    return students


def main():
    filename = input("Enter Prof. Jekyll's file name: ").strip()

    try:
        student_points = read_student_data(filename)

        # Sort by last name, then first name
        sorted_students = sorted(student_points.items(), key=lambda x: (x[0][1], x[0][0]))

        for (first_name, last_name), total_points in sorted_students:
            print(f"{first_name:10s} {last_name:10s} {total_points:.1f}")

    except StudentsDataException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
