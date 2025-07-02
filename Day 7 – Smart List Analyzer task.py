def analyze_numbers(numbers):
    # Manual sorting using Bubble Sort
    sorted_numbers = numbers[:]
    n = len(sorted_numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_numbers[j] > sorted_numbers[j+1]:
                sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]

    # Manual sum, min, max
    total = 0
    min_val = sorted_numbers[0]
    max_val = sorted_numbers[0]

    for num in sorted_numbers:
        total += num
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    average = total / n if n > 0 else 0

    return {
        "sorted": sorted_numbers,
        "sum": round(total, 2),
        "average": round(average, 2),
        "min": min_val,
        "max": max_val
    }

def print_dashboard(data):
    print("\n📊 Smart List Dashboard")
    for idx, (key, value) in enumerate(data.items(), 1):
        print(f"{idx}. {key} → {value}")

def get_user_numbers():
    while True:
        try:
            count = int(input("How many numbers would you like to enter? "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    numbers = []
    i = 0
    while i < count:
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
            i += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers

# Main Execution
if __name__ == "__main__":
    print("🔢 Welcome to Smart List Analyzer")
    user_numbers = get_user_numbers()
    stats = analyze_numbers(user_numbers)
    print_dashboard(stats)
