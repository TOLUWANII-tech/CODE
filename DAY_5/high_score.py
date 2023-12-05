student_scores = input('input a list of student scores').split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0

for score in student_scores:
    if score>high_score:
        high_score = score

print(f"The highest score in the class is: {high_score}")

#Youu can use the max(list_item) function to find the highest integer value in a list or min(list_item) to find the lowest number in a list