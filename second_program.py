# Questionno2
# Create an empty dictionary called dog
# • Add name, color, breed, legs, age to the dog dictionary
# • Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
#     • Get the length of the student dictionary
# • Get the value of skills and check the data type, it should be a list
# • Modify the skills values by adding one or two skills
# • Get the dictionary keys as a list
# • Get the dictionary values as a list

#creating an empty dictionary of dog
dog = {}

#adding key value pairs to the dog dictionary
dog = {'name':'Jessie', 'color':'white', 'breed':'Golden Retriver', 'legs':'4', 'age':'3'}

#creating a student dictionary
student = {'first_name':'Ajay', 'last_name': 'Veluru', 'gender':'male', 'age': '24', 'marital_status':'single',
           'skills':['Java'], 'country': 'India', 'city':'Cuddapah', 'address':'516390'}

#finding length of student dictionary
print(f"The length of student dictionay: {len(student)}")

#getting value of skills and checking datatype
print(type(student['skills']))

#adding new skills
student['skills'].extend(['gaming', 'dancing'])
print(student['skills'])

#printing keys and values for the student dictionary
print(f"The keys of student dictionary:{student.keys()}")
print(f"The values of student dictionary: {student.values()}")