'''
4 different core collection type
1. List
2.Tuple
3.Set
4. Dictionary


1.List
What is a list ?
Ordered
Mutable(Changeable)
Allows duplicate values


my_list=[10,20,30]
Key Characteristics:
1.Order is maintained
2.index-based access
3.changeable
4.Allows Duplicate values




2.Tuple :
Ordered
Immutable ( Cannot be chaqnged)
Allows duplicate values
my_tuple = (10,20,30)




Order Maintained
Index based access
immutable
allowed duplicate values
Faster than list


CRUD


config data
Fixed valued
safer
faster


Set :


Unordered
Mutable
Does not allow duplicate values
my_set={10,20,30}


Key Charateristics :
Order not maintained
no index based access
no duplicate accewss


Dictionary :


Stores Data in Key Value Pair
my_dict={
"name":"Karthick"
"age":35
"grade":"C"
}


Key-value structure
ordered
mutable
Duplicate Keys are not allowed
Duplicate values are allowed
'''
#Creation
data = [10,"Python",3.14,True]
#Read
print(data[1])
#Modify Data
data[1]="java"
print(data)


config=("localhost",3306,"admin")
print(config[0])




numbers={10,34,23,1,2,3,12,34,34,65}
print(numbers)


my_dict={
"name":"Karthick",
"age":35,
"grade":"C"
}


print(my_dict["grade"])
my_dict["City"]="Coimbatore"
print(my_dict)