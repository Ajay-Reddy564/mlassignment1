#Question6
# “I am a teacher and I love to inspire and teach people”
# • How many unique words have been used in the sentence? Use the split methods and set
# to get the unique words.

#string given
string = "I am a teacher and I love to inspire and teach people"
list = string.split(' ') #using the split method to find the no of words in the string sentence
print('unique words in that sentence:',list)

unique_count = len(set(list)) #finding the length count
print(f"number of unique words in the given string is:{unique_count}") #printing number of unique words