# Question3
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are
# fine)
# • Join brothers and sisters tuples and assign it to siblings
# • How many siblings do you have?
# • Modify the siblings tuple and add the name of your father and mother and assign it to
# family_members


#craeting sister and brother tuple
sister = ('Asritha', 'Suppu', 'Vijji', 'Sandhya', 'Bhavana')
brother = ('Mahesh', 'Kalyan', 'Shankar', 'Phani', 'Ram')

#join both brother and sister tubles
siblings = sister + brother

#taking count of siblings
print(f"Number of siblings: {len(siblings)}")

#modify tuple by adding father and mother names
temp = list(siblings)
temp.extend(['Hari','Lalitha'])
family_members = tuple(temp)
#printing all the family numbers
print(f"family members are:{family_members}") #printing all the family members both siblings, father and mother names