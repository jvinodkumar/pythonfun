from django.template.defaultfilters import upper,lower

# str len

str="hello"
print(len(str))

#upper
print(upper(str))
print(lower(str))

str1="world : str1"

str2 = str.format("test")
print(str2)

x = "x:hello".format(str1)
print(x+str2)


#Tuples and List

tuple = (1,2,3,4,5)
print(tuple)
print(tuple[0:2])


list=[1,2,3,4,5]
print(list)
print(list[0:2])
list.append(6)
print(list)
sublist = [7,8,9]
list.append(sublist)
print(list)
print(list[6])
list.pop(0)
print(list)

#Dictionary

person = dict(Name="vinod", Age="30", City="BLR")
print(person)
person["Name"]="rajesh"
person["Age"] = "32"
person["City"] = "Berlin"
print(person)

#type conversion
str = "10"
print(int(str))

#list range
list[:]=range(3)
print(list)
