student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum_of_heights = 0
length_of_list=0

for height in student_heights:
    sum_of_heights += height
    length_of_list +=1

print(f"Te average of ages is {sum_of_heights/length_of_list}")

#average = sum(student_heights)/len(student_heights)