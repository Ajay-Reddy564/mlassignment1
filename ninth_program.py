# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)
# Ex: L1: [150, 155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]
# Program which converts lbs to kgs for N number of students from user given inputs

# Here we are taking multiple inputs of weights from user in lbs
students_weight_in_lbs = list(map(int, input("Enter students weight here: ").split()))

students_weight_in_kgs = []

# Each input of students weight in lbs are multiplying with 0.435kg and storing in another list
# Here we know 1lb = 0.4535kg
for i in students_weight_in_lbs:
    lbs_to_kgs = i * 0.4535
    students_weight_in_kgs.append(lbs_to_kgs)

print('Students weight in lbs: ', students_weight_in_lbs)
print('Students weight in kgs: ', students_weight_in_kgs)