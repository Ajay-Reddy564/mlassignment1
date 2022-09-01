# Questionno1
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# • Sort the list and find the min and max age
# • Add the min age and the max age again to the list
# • Find the median age (one middle item or two middle items divided by two)
# • Find the average age (sum of all items divided by their number)
# • Find the range of the ages (max minus min)

#creating list of 10 students age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#sorting using built-in sort method
ages.sort()
print(f" Given list: {ages}") #printing sorted list of list ages

print(f"max age: {max(ages)}, min age: {min(ages)}") #printing min and max age

ages.extend([min(ages),max(ages)]) #here add the max and min ages back to the list
print(f"New list: {ages}") #printing the list after new additions

#finding the median
middle = int(len(ages)/2) #here we will find the middle index in the list
print(middle)
if middle % 2 == 0:    #we will find if the number is  even
    print(f"The median of ages: {int((ages[middle-1]  + ages[middle] )/ 2)}")

#here it will print average age
print(f"The average of ages: {sum(ages)/len(ages)}")

#here it will print the range
print(f"Range of the ages: {max(ages) - min(ages)}")