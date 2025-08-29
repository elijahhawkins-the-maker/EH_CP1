#EH_my_grades
grade_1 = int(input("what is your grade in your 1st class:   "))

grade_2 = int(input("what is your grade in your 2nd class:     "))

grade_3 = int(input("what is your grade in your 3rd class:   "))

grade_4 = int(input("what is your grade in your 4th class:    "))

grade_5 = int(input("what is your grade in your 5th class:   "))

grade_6 = int(input("what is your grade in your 6th class:   "))

grade_7 = int(input("and finally what is your grade for your 7th class:   "))

total_grade = grade_1 + grade_2 + grade_3 + grade_4 + grade_5 + grade_6 + grade_7
total_grade2 = (total_grade/7)
total_grade3 = round(total_grade2, 2)
print("your average grade is", total_grade3)