'''
#Create dictionary
student={"name": "Zulfikhar", "age": "44", "city": "Para", "phone": "123456789", "Roleno": "666"}

print(student)

print(student["name"])

#Add key
student["town"]= "Accaribo"

print(student)

#Update key
student["Roleno"]= "999"
print(student)

#Remove town
student.pop("town")
print(student)

#Remove last item
student.popitem()
print(student)

#iterate through the dictionary
#keys
for k in student:
    print(k)

#values
for v in student.values():
    print(v)

#both keys and values
for k,v in student.items():
    print(k,v)

#Student record list inside a dictionary
studentRecord = {
    "name": "Zulfikhar",
    "age": "44",
    "marks": [78,86,95]

}
print(studentRecord["marks"][0])

#Dicitonary of dictionaries
employees = {
    "E0101": {"name":"Zulfikhar", "salary":60000},
    "E0102": {"name":"Gianna", "salary":80000},
    "E0103": {"name":"Xenia", "salary":100000},
}
print(employees["E0103"]["name"])

#Exercise mentor
#1. Create a dictionary storage for 3 persons: name, age, city, skills - list
#2. Add a new key, 3. Update the city, 4. print all the keys, 5. delete skills
#6. Loop and print all key values pairs

persons = {
    "P0101": {"name":"Anna", "age":"34", "city":"Chicago","skills":["fast", "smart", "precise"]}
    "P0102": {"name":"Elsa", "age":"35", "city":"Texas", "skills":["fast", "smart", "precise"]}
}
'''


'''
#Next topic
#count the character frequency

text = "apple"
freq = {}

for ch in text:
    if ch in freq:
      freq[ch]+=1; #increasing the count
    else:
        freq[ch]=1 # first time, get the count to 1
print(freq)
'''



