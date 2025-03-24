def student_grade(score):
    if 0 <= score <= 49:
        return "not good"
    elif 50 <= score <= 69:
        return "Normal"
    elif 70 <= score <= 89:
        return "Good"
    elif 90 <= score <= 100:
        return "Perfect"
    else:
        return "Incorent score"

score = int(input("Enter student score form 1 to 100: "))
print(f"Student score: {student_grade(score)}")
