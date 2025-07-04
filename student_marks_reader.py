def read_student_marks(file_path):
    student_marks = {}
    skipped_entries = 0

    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    print(f"[Line {line_num}] Skipped: Empty line")
                    skipped_entries += 1
                    continue

                try:
                    name, mark = line.split(',')
                    name = name.strip()
                    mark = mark.strip()

                    if not name or not mark:
                        raise ValueError("Missing name or mark")

                    mark = int(mark)
                    student_marks[name] = mark

                except ValueError as ve:
                    print(f"[Line {line_num}] Skipped: {ve}")
                    skipped_entries += 1

    except FileNotFoundError:
        raise

    return student_marks, skipped_entries


def print_student_data(student_marks):
    try:
        if not student_marks:
            raise ZeroDivisionError("No valid student data to display.")

        total = sum(student_marks.values())
        average = total / len(student_marks)

        print("\n🎓 Student Marks:")
        for name, mark in student_marks.items():
            print(f"{name}: {mark}")

        print(f"\n📊 Average Mark: {average:.2f}")

    except ZeroDivisionError as ze:
        print(f"⚠️ {ze}")


def main():
    while True:
        file_path = input("📁 Enter the path to the marks.txt file: ").strip()

        try:
            student_marks, skipped = read_student_marks(file_path)
            print_student_data(student_marks)
            print(f"\n✅ Total Valid Entries: {len(student_marks)}")
            print(f"❌ Skipped Entries: {skipped}")
            break  # Exit loop if successful

        except FileNotFoundError:
            print("🚫 File not found! Please enter a valid file path.\n")

if __name__ == "__main__":
    main()
