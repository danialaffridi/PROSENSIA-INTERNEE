# GPA Calculator using Functional Design

# Grade to point mapping dictionary
GRADE_POINTS = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'F': 0.0
}

def calculate_weighted_gpa(grades):
    """
    Calculate the weighted GPA based on a list of (grade, credit_hour) tuples.
    """
    total_points = 0
    total_credits = 0

    for grade, credit in grades:
        grade_point = GRADE_POINTS.get(grade.upper(), 0.0)
        total_points += grade_point * credit
        total_credits += credit

    if total_credits == 0:
        return 0.0

    gpa = total_points / total_credits
    return round(gpa, 2)

def print_gpa_summary(student_name, gpa):
    """
    Print a formatted GPA summary.
    """
    print(f"Student {student_name} has GPA: {gpa:.2f}")

# Example usage with named arguments
example_grades = [('A', 3), ('B+', 4), ('C', 2)]
student_name = "Rania"
gpa_result = calculate_weighted_gpa(example_grades)
print_gpa_summary(student_name=student_name, gpa=gpa_result)
