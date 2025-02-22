Employee = {
    'id':1,
    'Name':'Saurabh',
    'Gender':'Male',
    'Dept':'IT',
    'Salary':50000,
    'Desg':'Junior software developer',
    'Address':'Delhi'
}

# print(Employee)
# print()
# print(Employee["Name"])
# print()
# print(Employee["Address"])
# print()
# print(Employee.keys)
# print()
# print(Employee.values)


# dict1 = {'emp1': 'Saurabh', 'emp2': 'Tony', 'emp3': 'Rohan', 'emp4': 'Nitu', 'emp5': 'Aditya'}
# new_dict = {}
# for key in dict1:
#     new_dict[key] = dict1[key]
# print(new_dict)


test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
sum = 0
for key in test_dict:
   sum = sum + test_dict[key]
result = sum / 5
# print(result)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={*dic1,dic2,*dic3}
# print(dic4)



# dict = {1:10,2:20,3:30,4:40,5:50,6:60}

# for key, value in dict.items():
    # print(f"{key} \t {value}")



# # Original dictionary
# dictt = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

# # Identify keys with None values
# keys_to_remove = [key for key, value in dictt.items() if value is None]

# # Remove identified keys
# for key in keys_to_remove:
#     del dictt[key]

# print(dictt)