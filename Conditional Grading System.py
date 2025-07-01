def evaluate_grade(score: float) -> str:
    """Converts numeric score to letter grade using conditionals."""
    if score > 100 or score < 0:
        return "Invalid"
    if score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def print_grade_summary(student_name: str = 'Unnamed', score: float = 0.0):
    """Prints a formatted grade summary for a student."""
    grade = evaluate_grade(score)
    if grade == "Invalid":
        print(f"Invalid score for {student_name}. Please enter a value between 0 and 100.")
    else:
        print(f"Student {student_name} scored {score} → Grade: {grade}")

# Example usage
print_grade_summary(student_name='Zara', score=87.5)
print_grade_summary(student_name='Ali', score=45)
print_grade_summary(student_name='Sara', score=105)  # Invalid example
