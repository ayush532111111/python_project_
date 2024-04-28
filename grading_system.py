def awful_grading_system(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    elif score >= 50:
        grade = 'E'
    else:
        return "Sorry, you have failed!"

    return f"Your grade is: {grade}"

def main():
    try:
        score = float(input("Enter your score: "))
        if score < 0 or score > 100:
            print("Invalid score! Please enter a score between 0 and 100.")
            return
        print(awful_grading_system(score))
    except ValueError:
        print("Invalid input! Please enter a numerical value.")

if __name__ == "__main__":
    main()
