# 🐍 Day 4 – Student Record System using Tuples & Sets

# Step 1: Create an immutable tuple of student IDs
student_ids = ("S001", "S002", "S003", "S004")
print("Student IDs (Immutable):", student_ids)

# Step 2: Create a set of unique course names
courses = {"Python", "AI", "ML"}
print("\nInitial Courses Offered:", courses)

# Step 3: Add a new course to the set
courses.add("Data Science")
print("\nCourse 'Data Science' added:", courses)

# Step 4: Attempt to add a duplicate course (will not change the set)
courses.add("AI")
print("\nAttempted to add duplicate course 'AI':", courses)

# Step 5: Remove a course from the set
courses.remove("ML")  # Remove 'ML' if it exists
print("\nCourse 'ML' removed:", courses)

# Step 6: Display all final courses
print("\nFinal Course List:", courses)

# Step 7: Display student IDs with enrolled courses (just for display demo)
for i, student in enumerate(student_ids):
    print(f"Student {student} is enrolled in {list(courses)[i % len(courses)]}")
